from sqlalchemy import (
    Column,
    String,
    Integer,
    Boolean,
    Date,
    JSON,
    BigInteger,
    ARRAY,
)
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import Engine

Base = declarative_base()

# https://docs.sqlalchemy.org/en/20/orm/quickstart.html#declare-models
class Tweet(Base):
    __tablename__ = "tweets"
    id = Column(String(20), primary_key=True)
    #
    ## AGREGAR ATRIBUTOS
    #

def setup(engine: Engine):
    Base.metadata.create_all(engine, checkfirst=True)


def insert_many(tweet: list[dict], engine: Engine):
    # https://docs.sqlalchemy.org/en/20/orm/session_basics.html
    print("Insertar tweet no implmentado")
    #
    ## COMPLETAR
    #