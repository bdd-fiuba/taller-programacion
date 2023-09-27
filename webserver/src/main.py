from fastapi import FastAPI, Response
from json import dumps as json_dumps

from .database import init_db, get_from_collection
from .response_tweet import ResponseTweet
from .response_car import ResponseCar


app = FastAPI(
    title="Tweets DB API",
    description="API de guardado y acceso a tweets, utilizando: MongoDB",
)
conn = init_db()


@app.get("/tweets", tags=["tweet"], response_model=list[ResponseTweet])
async def get_tweet(skip: int = 0, limit: int = 10):
    print(f"Buscando: desde {skip} hasta {skip + limit}")
    tweets = await get_from_collection("tweets", skip, limit, conn)
    if tweets is None:
        return Response(
            status_code=404,
            content=f"No existen tweets en el intervalo {skip} - {skip + limit}",
        )
    print(f"Returning like {tweets[0]}")
    return Response(
        status_code=200,
        content=json_dumps(tweets, indent=4, sort_keys=True, default=str),
    )


@app.get("/cars", tags=["cars"], response_model=list[ResponseCar])
async def get_car(skip: int = 0, limit: int = 10):
    print(f"Buscando: desde {skip} hasta {skip + limit}")
    cars = await get_from_collection("cars", skip, limit, conn)
    if cars is None:
        return Response(
            status_code=404,
            content=f"No existen autos en el intervalo {skip} - {skip + limit}",
        )
    return Response(
        status_code=200,
        content=json_dumps(cars, indent=4, sort_keys=True, default=str),
    )


@app.exception_handler(404)
async def not_found(_request, _exc):
    return Response(status_code=302, headers={"Location": "/docs"})


@app.exception_handler(Exception)
async def exception_handler(_request, exc):
    return Response(status_code=500, content=repr(exc))
