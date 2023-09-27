import click
import requests

from .utils import get_host, get_port
from .postgres.utils import init_db, insert_into

HOST = get_host()
PORT = get_port()
engine = init_db()


@click.command()
@click.argument("collection", type=click.Choice(["cars", "tweets"]))
@click.option("--skip", default=0, help="Skip")
@click.option("--limit", default=10, help="Limit")
def extract(collection: str, skip: int, limit: int):
    res = requests.get(f"http://{HOST}:{PORT}/{collection}?skip={skip}&limit={limit}")
    if res.status_code != 200:
        print(f"Error: {res.status_code}")
        print(res.text)
        return
    tweets = res.json()
    print(f"Obtenidos {len(tweets)} resultados")
    print([tweet["id"] for tweet in tweets[:5]])
    insert_into(collection, tweets, engine)


def main():
    extract()


if __name__ == "__main__":
    main()
