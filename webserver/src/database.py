"""
Archivo con funciones a completar de conexión
a la base de datos
"""
import json
from pathlib import Path
from typing import Optional
from pymongo import MongoClient
from pymongo.database import Database

DBConn = Database
MONGO_URL = "mongodb://admin:admin@mongodb:27017"
MONGO_DBNAME = "taller"


def load_data(db: DBConn):
    print("Loading data")
    data_path = Path(__file__).parent.parent / "data"
    for collection in ["tweets", "cars"]:
        collection_path = data_path / f"{collection}.json"
        db[collection].create_index("_id")
        with open(collection_path) as f:
            values = [json.loads(line) for line in f]
            data = {value["_id"]: value for value in values}
            to_remove = []
            for key in data.keys():
                if db[collection].find_one({"_id": key}):
                    to_remove.append(key)
            for key in to_remove:
                del data[key]
            if data:
                db[collection].insert_many(data.values())

        print("Cargada información de", collection)


def init_db() -> DBConn:
    client = MongoClient(MONGO_URL)
    db = client[MONGO_DBNAME]
    load_data(db)
    print("MongoDB connected")
    return db


async def get_from_collection(
    collection: str, skip: int, limit: int, db: DBConn
) -> Optional[list[dict]]:
    data = db[collection].find({}).sort("created_at").skip(skip).limit(limit)

    def replace_id(item):
        item["id"] = item["_id"]
        del item["_id"]
        return item

    items = [replace_id(item) for item in data]
    if not items:
        return None
    return items
