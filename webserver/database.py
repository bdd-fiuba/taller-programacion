"""
Archivo con funciones a completar de conexión
a la base de datos
"""
from typing import Optional
from pymongo import MongoClient
from pymongo.collection import Collection

DBConn = Collection
MONGO_URL = "mongodb://admin:admin@mongodb:27017"
MONGO_DBNAME = "taller"


def init_db() -> DBConn:
    client = MongoClient(MONGO_URL)
    db = client[MONGO_DBNAME]
    col = db["tweets"]
    return col


async def load_tweet(tweet: dict, conn: DBConn):
    conn.update_one({"_id": tweet["_id"]}, {"$set": tweet}, upsert=True)


async def get_tweet(id, conn: DBConn) -> Optional[dict]:
    tweet = conn.find_one({"_id": id})
    return tweet
