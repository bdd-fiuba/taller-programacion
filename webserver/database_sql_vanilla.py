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


def init_db() -> DBConn:
    engine = create_engine(POSTGRES_URL)
    conn = engine.connect()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tweets (
            id VARCHAR(20) PRIMARY KEY,
            contributors VARCHAR(20),
            cooccurrence_checked BOOLEAN NOT NULL,
            coordinates JSON,
            created_at  DATE NOT NULL,
            display_text_range BIGINT[2],
            entities JSON NOT NULL,
            favorite_count BIGINT NOT NULL,
            full_text VARCHAR(1000) NOT NULL,
            geo JSON,
            hashtag_origin_checked BOOLEAN NOT NULL,
            in_reply_to_screen_name VARCHAR(50),
            in_reply_to_status_id BIGINT,
            in_reply_to_status_id_str VARCHAR(20),
            in_reply_to_user_id BIGINT,
            in_reply_to_user_id_str VARCHAR(20),
            in_user_hashtag_collection BOOLEAN NOT NULL,
            is_quote_status BOOLEAN NOT NULL,
            lang VARCHAR(5) NOT NULL,
            place JSON,
            retweet_count BIGINT NOT NULL,
            retweeted_status JSON,
            source VARCHAR(100) NOT NULL,
            text VARCHAR(1000) NOT NULL,
            truncated BOOLEAN NOT NULL,
            "user" JSON NOT NULL,
            user_id VARCHAR(20) NOT NULL
        );
    """
    )
    return engine

JSON_FIELDS = [
    "coordinates",
    "entities",
    "geo",
    "place",
    "retweeted_status",
    "user",
]
STR_FIELDS = [
    "id",
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


async def load_tweet(tweet: dict, conn: DBConn):
    print(tweet)
    fix_string_fields(tweet)
    fix_json_fields(tweet)
    fix_int_array_fields(tweet)
    insert = """INSERT INTO tweets VALUES (
        {id},
        {contributors},
        {cooccurrence_checked},
        {coordinates},
        {created_at},
        {display_text_range},
        {entities},
        {favorite_count},
        {full_text},
        {geo},
        {hashtag_origin_checked},
        {in_reply_to_screen_name},
        {in_reply_to_status_id},
        {in_reply_to_status_id_str},
        {in_reply_to_user_id},
        {in_reply_to_user_id_str},
        {in_user_hashtag_collection},
        {is_quote_status},
        {lang},
        {place},
        {retweet_count},
        {retweeted_status},
        {source},
        {text},
        {truncated},
        {user},
        {user_id}
    ) ON CONFLICT (id) DO NOTHING;
    """.format(**tweet).replace('None', 'null').replace('%', '%%')
    print()
    print(insert)
    print()
    conn.execute(insert)
    print('inserted')


async def get_tweet(id: str, conn: DBConn) -> tuple[bool, Optional[dict]]:
    result = conn.execute(
        f"""
        SELECT * FROM tweets WHERE id = '{id}';
    """
    )
    if result.rowcount == 0:
        return None
    tweet = result.fetchone()
    return tweet
