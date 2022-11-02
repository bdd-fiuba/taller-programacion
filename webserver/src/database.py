"""
Archivo con funciones a completar de conexión
a la base de datos
"""
from typing import Optional
from sqlalchemy import (
    create_engine,
    Column,
    String,
    Integer,
    Boolean,
    Date,
    JSON,
    BigInteger,
    ARRAY,
)
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


DBConn = Engine
POSTGRES_URL = "postgresql+psycopg2://admin:admin@postgres:5432/admin"

Base = declarative_base()


# https://docs.sqlalchemy.org/en/20/orm/quickstart.html#declare-models
class SqlTweet(Base):
    __tablename__ = "tweets"
    id = Column(String(20), primary_key=True)


def init_db() -> DBConn:
    engine = create_engine(POSTGRES_URL)
    # https://docs.sqlalchemy.org/en/20/orm/quickstart.html#emit-create-table-ddl

async def load_tweet(tweet: dict, conn: DBConn):
    # https://docs.sqlalchemy.org/en/20/orm/session_basics.html
    tweet['id'] = tweet['_id']
    del tweet['_id']
    raise NotImplementedError()


async def get_tweet(id: str, conn: DBConn) -> Optional[dict]:
    return None
