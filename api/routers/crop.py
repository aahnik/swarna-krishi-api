import string
import random

from fastapi import APIRouter, HTTPException, Depends, Response, status
from typing import List
from api.models.crop import CropIn, CropOut, Crop
from api.models.user import UserInDB
from api.utils.current_user import GcauDep
from api.utils.exceptions import (
    crop_not_found_exc,
)
from datetime import datetime
from beanie import PydanticObjectId


router = APIRouter(prefix="/crop", tags=["Crops"])


@router.get("/all")
async def list_crops(
    user: GcauDep,
) -> List[CropOut | None]:
    return await Crop.find(Crop.user.id == user.id).project(CropOut).to_list()


@router.post("/new")
async def add_new_crop(crop_in: CropIn, user: GcauDep) -> PydanticObjectId:
    crop = Crop(**crop_in.dict(), user=user)
    await crop.insert()
    return crop.id


@router.patch("/update/{crop_id}")
async def update_crop(user: GcauDep, crop_id: PydanticObjectId, crop_update: CropIn):
    crop = await Crop.get(crop_id)
    if not crop:
        raise crop_not_found_exc
    crop = crop.copy(update=crop_update.dict(exclude_unset=True))
    await crop.save()
    return crop.id


@router.delete("/delete/{crop_id}")
async def delete_crop(user: GcauDep, crop_id: PydanticObjectId):
    crop = await Crop.get(crop_id)
    if not crop:
        raise crop_not_found_exc
    await crop.delete()
    return {"message": "successfully deleted crop"}
