"""
Archivo con funciones a completar de conexión
a la base de datos
"""
from json import dumps as json_dumps
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Connection
from typing import Optional

DBConn = Connection
POSTGRES_URL = "postgresql+psycopg2://admin:admin@postgres:5432/admin"


JSON_FIELDS = [
    "coordinates",
    "entities",
    "geo",
    "place",
    "retweeted_status",
    "user",
]
STR_FIELDS = [
    "_id",
    "contributors",
    "full_text",
    "in_reply_to_screen_name",
    "in_reply_to_status_id_str",
    "in_reply_to_user_id_str",
    "lang",
    "source",
    "text",
    "user_id",
]
DATE_FIELDS = ["created_at"]
BOOOLEAN_FIELDS = [
    "cooccurrence_checked",
    "hashtag_origin_checked",
    "in_user_hashtag_collection",
    "is_quote_status",
    "truncated",
]
INT_FIELDS = [
    "favorite_count",
    "retweet_count",
    "in_reply_to_status_id",
    "in_reply_to_user_id",
]
INT_ARRAY_FIELDS = ["display_text_range"]


def fix_string_fields(tweet: dict):
    for field in STR_FIELDS + DATE_FIELDS:
        value = tweet[field]
        if value is not None:
            value = str(value).replace("\'", "\'\'")
            tweet[field] = f"'{value}'"

def fix_json_fields(tweet: dict):
    for field in JSON_FIELDS:
        value = tweet[field]
        if value is not None:
            value = json_dumps(value).replace("'", "''")
            tweet[field] = f"'{value}'"


def fix_int_array_fields(tweet: dict):
    for field in INT_ARRAY_FIELDS:
        value = tweet[field]
        if value is not None:
            value = str(value).replace("[", "{").replace("]", "}")
            tweet[field] = f"'{value}'"


def init_db() -> DBConn:
    pass

async def load_tweet(tweet: dict, conn: DBConn):
    raise NotImplementedError()


async def get_tweet(id: str, conn: DBConn) -> Optional[dict]:
    return None
