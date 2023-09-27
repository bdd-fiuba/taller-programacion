from pydantic import BaseModel, Field
from typing import List


def _get_example():
    return {
        "id": "BC 456 DE",
        "brand": "Ford",
        "model": "F-150",
        "year": 2022,
        "owner": {"id": "54321098", "name": "Mike Johnson"},
        "amenities": ["4WD", "Towing Package", "Touchscreen Infotainment"],
    }


class Owner(BaseModel):
    id: str
    name: str


class ResponseCar(BaseModel):
    id: str = Field(alias="_id")
    brand: str
    model: str
    year: int
    owner: Owner
    amenities: List[str]

    class Config:
        schema_extra = {"example": [_get_example()]}
