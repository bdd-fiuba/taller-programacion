import requests
from sys import argv
from json import dumps as json_dumps


def buscar_tweet(id: str):
    res = requests.get(f"http://localhost:8000/tweet/{id}")
    if res.status_code != 200:
        print(f"Error: {res.status_code}")
        print(res.text)
    else:
        print(json_dumps(res.json(), indent=2))


def main():
    if len(argv) != 2:
        raise ValueError("Se debe pasar el id de tweet")
    buscar_tweet(argv[1])


if __name__ == "__main__":
    main()
