"""Conexión a la base de datos"""

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from os import getenv

from .cars import setup as setup_cars, insert_many as insert_cars
from .tweets import setup as setup_tweets, insert_many as insert_tweets



def get_host():
    return (
        "localhost"
        if getenv("IS_CONTAINER", "false").lower() == "false"
        else "postgres"
    )


def get_port():
    return 7515

HOST = get_host()
PORT = get_port()
POSTGRES_URL = f"postgresql+psycopg2://admin:admin@{HOST}:{PORT}/admin"


def setup_db(engine: Engine):
    setup_cars(engine)
    setup_tweets(engine)


def init_db() -> Engine:
    engine = create_engine(POSTGRES_URL)
    setup_db(engine)
    print("Conectado a la base de datos")
    return engine


def insert_into(collection: str, data: list, engine: Engine):
    if collection == "cars":
        insert = insert_cars
    elif collection == "tweets":
        insert = insert_tweets

    insert(data, engine)