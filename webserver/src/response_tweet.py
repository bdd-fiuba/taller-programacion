from datetime import datetime
from json import load as json_load
from pathlib import Path
from pydantic import BaseModel, validator, Field
from typing import Optional, List, Literal, Union


def _get_example():
    example_path = Path(__file__).parent.absolute() / "tweet_example.json"
    if not example_path.exists():
        return None
    with open(example_path, "r") as f:
        return json_load(f)


class GeoCoordinates(BaseModel):
    type: Literal["Point", "LineString", "Polygon"]
    coordinates: Union[List[float], List]


class WithIndices(BaseModel):
    indices: List[int]

    @validator("indices")
    def indices_must_be_2(cls, v):
        assert len(v) == 2
        return v

    @validator("indices")
    def indices_must_be_increasing(cls, v):
        assert v[0] < v[1]
        return v


class Hashtag(WithIndices):
    text: str


class Symbol(BaseModel):
    text: str


class UserMention(BaseModel):
    screen_name: str
    name: str
    id: int
    id_str: str


class Url(WithIndices):
    url: str
    expanded_url: str
    display_url: str


class Entities(BaseModel):
    hashtags: List[Hashtag]
    symbols: List[Symbol]
    user_mentions: List[UserMention]
    urls: List[Url]
    media: Optional[List]


class Place(BaseModel):
    id: str
    url: str
    place_type: str
    name: str
    full_name: str
    country_code: str
    country: str
    contained_within: List
    bounding_box: GeoCoordinates
    attributes: dict


class User(BaseModel):
    id_str: str
    name: str
    screen_name: str
    location: str
    description: str
    url: Optional[str]
    protected: bool
    followers_count: int
    friends_count: int
    listed_count: int
    created_at: str
    favourites_count: int
    time_zone: Optional[str]
    verified: bool
    statuses_count: int
    lang: Optional[str]
    default_profile: bool


class ResponseTweet(BaseModel):
    id: str = Field(alias="_id")
    contributors: Optional[str]
    cooccurrence_checked: bool
    coordinates: Optional[GeoCoordinates]
    created_at: datetime
    display_text_range: List[int]
    entities: Entities
    favorite_count: int
    full_text: str
    geo: Optional[GeoCoordinates]
    hashtag_origin_checked: bool
    in_reply_to_screen_name: Optional[str]
    in_reply_to_status_id: Optional[int]
    in_reply_to_status_id_str: Optional[str]
    in_reply_to_user_id: Optional[int]
    in_reply_to_user_id_str: Optional[str]
    in_user_hashtag_collection: bool
    is_quote_status: bool
    lang: str
    place: Optional[Place]
    retweet_count: int
    retweeted_status: Optional[dict]
    source: str
    text: str
    truncated: bool
    user: User
    user_id: str

    class Config:
        schema_extra = {"example": [_get_example()]}
