import requests
from sys import argv
from json import loads as json_loads


def iterador_tweets():
    with open("data/tweets.json", "r", encoding="utf-8") as f:
        yield from f


def cargar_tweets(count):
    i = 0
    with_errors = 0
    error_ids = []
    for tweet_str in iterador_tweets():
        tweet = json_loads(tweet_str)
        res = requests.post("http://localhost:8000/tweet/create", json=tweet)
        if res.status_code != 201:
            with_errors += 1
            error_ids.append(tweet["_id"])
            print(f"Error al cargar tweet: {tweet['_id']}")
            print(res.text)
        i += 1
        if i % 100 == 0:
            percent_done = 0 if count is None else i / count * 100
            print(f"( {percent_done:.02f} % )")
        if count is not None and i >= count:
            break
    print(f"Errores: {with_errors}")
    print(f"Errores ids: {error_ids}")
    return i


def main():
    count = None
    if len(argv) > 1:
        count = int(argv[1])
    total = cargar_tweets(count)
    print(f"Cargados {total} tweets")


if __name__ == "__main__":
    main()
