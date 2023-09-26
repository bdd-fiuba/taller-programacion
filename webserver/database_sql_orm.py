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
    contributors = Column(String(20))
    cooccurrence_checked = Column(Boolean, nullable=False)
    coordinates = Column(JSON)
    created_at = Column(Date, nullable=False)
    display_text_range = Column(ARRAY(BigInteger))
    entities = Column(JSON, nullable=False)
    favorite_count = Column(BigInteger, nullable=False)
    full_text = Column(String(1000), nullable=False)
    geo = Column(JSON)
    hashtag_origin_checked = Column(Boolean, nullable=False)
    in_reply_to_screen_name = Column(String(50))
    in_reply_to_status_id = Column(BigInteger)
    in_reply_to_status_id_str = Column(String(20))
    in_reply_to_user_id = Column(BigInteger)
    in_reply_to_user_id_str = Column(String(20))
    in_user_hashtag_collection = Column(Boolean, nullable=False)
    is_quote_status = Column(Boolean, nullable=False)
    lang = Column(String(5), nullable=False)
    place = Column(JSON)
    retweet_count = Column(BigInteger, nullable=False)
    retweeted_status = Column(JSON)
    source = Column(String(100), nullable=False)
    text = Column(String(1000), nullable=False)
    truncated = Column(Boolean, nullable=False)
    user = Column(JSON, nullable=False)
    user_id = Column(String(20), nullable=False)

    def __repr__(self) -> str:
        return f"Tweet(id={self.id}, created_at={self.created_at})"


def init_db() -> DBConn:
    engine = create_engine(POSTGRES_URL)
    # https://docs.sqlalchemy.org/en/20/orm/quickstart.html#emit-create-table-ddl
    Base.metadata.create_all(engine, checkfirst=True)
    return engine


async def load_tweet(tweet: dict, conn: DBConn):
    # https://docs.sqlalchemy.org/en/20/orm/session_basics.html
    with Session(conn) as session:
        # insert
        # session.add(SqlTweet(**tweet))
        # upsert 
        session.merge(SqlTweet(**tweet))
        session.commit()


async def get_tweet(id: str, conn: DBConn) -> tuple[bool, Optional[dict]]:
    with Session(conn) as session:
        tweet = session.query(SqlTweet).filter_by(id=id).first()
    if tweet is None:
        return False, None
    tweet_dict = {
        'id': tweet.id,
        'contributors': tweet.contributors,
        'cooccurrence_checked': tweet.cooccurrence_checked,
        'coordinates': tweet.coordinates,
        'created_at': tweet.created_at,
        'display_text_range': tweet.display_text_range,
        'entities': tweet.entities,
        'favorite_count': tweet.favorite_count,
        'full_text': tweet.full_text,
        'geo': tweet.geo,
        'hashtag_origin_checked': tweet.hashtag_origin_checked,
        'in_reply_to_screen_name': tweet.in_reply_to_screen_name,
        'in_reply_to_status_id': tweet.in_reply_to_status_id,
        'in_reply_to_status_id_str': tweet.in_reply_to_status_id_str,
        'in_reply_to_user_id': tweet.in_reply_to_user_id,
        'in_reply_to_user_id_str': tweet.in_reply_to_user_id_str,
        'in_user_hashtag_collection': tweet.in_user_hashtag_collection,
        'is_quote_status': tweet.is_quote_status,
        'lang': tweet.lang,
        'place': tweet.place,
        'retweet_count': tweet.retweet_count,
        'retweeted_status': tweet.retweeted_status,
        'source': tweet.source,
        'text': tweet.text,
        'truncated': tweet.truncated,
        'user': tweet.user,
        'user_id': tweet.user_id
    }
    return False, tweet_dict
