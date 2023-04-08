from beanie import Document, Indexed, Link
from pydantic import BaseModel, Field
from typing import List, Tuple
from api.models.user import UserInDB
from datetime import datetime
from enum import Enum
from beanie import PydanticObjectId




class SoilColors(str, Enum):
    red = "red"
    black = "black"
    white = "white"
    yellow = "yellow"
    brown = "brown"
    green = "green"


class SoilTexture(str, Enum):
    sandy = "sandy"
    sandy_loam = "sandy_loam"
    loam = "loam"
    silty_loam = "silty_loam"
    clay_loam = "clay_loam"
    clay = "clay"
    heavy_clay = "heavy_clay"


class LandIn(BaseModel):
    name: str
    nitrogen: float | None
    phosphorous: float | None
    potassium: float | None
    ph: float | None
    city: str | None
    rainfall: float | None
    soil_color: SoilColors | None
    soil_texture: SoilTexture | None


class LandOut(LandIn):
    id: PydanticObjectId = Field(alias="_id")


class Land(Document, LandOut):
    user: Link[UserInDB]
