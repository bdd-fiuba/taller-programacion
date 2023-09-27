from datetime import datetime
from json import load as json_load
from pathlib import Path
from pydantic import BaseModel, Field
from typing import Any


def _get_example():
    example_path = Path(__file__).parent.absolute() / "tweet_example.json"
    if not example_path.exists():
        return None
    with open(example_path, "r") as f:
        return json_load(f)


class Tweet(BaseModel):
    id: Any = Field(alias="_id")
    contributors: Any
    cooccurrence_checked: Any
    coordinates: Any
    created_at: Any
    display_text_range: Any
    entities: Any
    favorite_count: Any
    full_text: Any
    geo: Any
    hashtag_origin_checked: Any
    in_reply_to_screen_name: Any
    in_reply_to_status_id: Any
    in_reply_to_status_id_str: Any
    in_reply_to_user_id: Any
    in_reply_to_user_id_str: Any
    in_user_hashtag_collection: Any
    is_quote_status: Any
    lang: Any
    place: Any
    retweet_count: Any
    retweeted_status: Any
    source: Any
    text: Any
    truncated: Any
    user: Any
    user_id: Any

    class Config:
        schema_extra = {"example": _get_example()}


def tweet_to_dict(tweet: Tweet):
    return tweet.dict(by_alias=True, exclude_none=False)
