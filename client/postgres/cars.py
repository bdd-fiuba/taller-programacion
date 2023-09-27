import json
from sqlalchemy.engine import Engine

CREATE_CARS_TABLE = """CREATE TABLE IF NOT EXISTS cars (
    id VARCHAR(9) PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INTEGER NOT NULL,
    owner JSON NOT NULL
);
"""

INSERT_INTO_CARS = """INSERT INTO cars
VALUES ('{id}', '{brand}', '{model}', {year}, '{owner}')
ON CONFLICT (id) DO UPDATE
SET brand='{brand}', model='{model}', year={year}, owner='{owner}';
"""


def setup(engine: Engine):
    engine.connect().execute(CREATE_CARS_TABLE)


def insert_many(cars: list[dict], engine: Engine):
    for car in cars:
        engine.connect().execute(
            INSERT_INTO_CARS.format(
                id=car["id"],
                brand=car["brand"],
                model=car["model"],
                year=car["year"],
                owner=json.dumps(car["owner"]),
            )
        )
