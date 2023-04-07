from beanie import Document, Indexed, Link
from pydantic import BaseModel, Field
from typing import List
from api.models.user import UserInDB
from datetime import datetime
from enum import Enum
from beanie import PydanticObjectId


class CropIn(BaseModel):
    crop_name: str
    irrigation_interval_days: int | None = None  # in days
    fertilization_interval_days: int | None = None  # in days
    soil_type: str | None = None
    sow_time: datetime | None = None
    harvest_time: datetime | None = None  # in months


class CropOut(CropIn):
    id: PydanticObjectId = Field(alias="_id")


class Crop(Document, CropOut):
    user: Link[UserInDB]
