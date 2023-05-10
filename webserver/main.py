from fastapi import FastAPI, Response
from json import dumps as json_dumps

from webserver.database import init_db, load_tweet, get_tweet
from webserver.tweet import Tweet, tweet_to_dict
from webserver.response_tweet import ResponseTweet


app = FastAPI(
    title="Tweets DB API",
    description="API de guardado y acceso a tweets, utilizando: MongoDB",
)
conn = init_db()


@app.post(
    "/tweet/create",
    tags=["tweet"],
    status_code=201,
    responses={201: {"description": "Tweet creado correctamente"}},
)
async def post_tweet(tweet: Tweet):
    await load_tweet(tweet_to_dict(tweet), conn)
    return Response(status_code=201)



@app.get("/tweet/{id}", tags=["tweet"], response_model=ResponseTweet)
async def get_tweet_(id: str):
    print(f"Buscando: {id}")
    tweet = await get_tweet(id, conn)
    if tweet is None:
        return Response(status_code=404, content="Tweet no encontrado")
    return Response(status_code=200, content=json_dumps(tweet, indent=4, sort_keys=True, default=str))


@app.exception_handler(404)
async def not_found(_request, _exc):
    return Response(status_code=302, headers={"Location": "/docs"})


@app.exception_handler(Exception)
async def exception_handler(_request, exc):
    return Response(status_code=500, content=repr(exc))
