"""
Archivo con funciones a completar de conexión
a la base de datos
"""
from typing import Optional

DBConn = None


def init_db() -> DBConn:
    pass

async def load_tweet(tweet: dict, conn: DBConn):
    raise NotImplementedError()


async def get_tweet(id: str, conn: DBConn) -> Optional[dict]:
    return None
