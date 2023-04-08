import string
import random

from fastapi import APIRouter, HTTPException, Depends, Response, status
from typing import List
from api.models.land import Land, LandIn, LandOut
from api.models.user import UserInDB
from api.utils.current_user import GcauDep
from api.utils.exceptions import land_not_found_exc
from datetime import datetime
from beanie import PydanticObjectId
from api.harvestify import predictor
from api.utils.exceptions import land_missing_details_exc
router = APIRouter(prefix="/land", tags=["Lands"])


@router.get("/all")
async def list_crops(
    user: GcauDep,
) -> List[LandOut | None]:
    return await Land.find(Land.user.id == user.id).project(LandOut).to_list()


@router.post("/new")
async def add_new_land(land_in: LandIn, user: GcauDep) -> PydanticObjectId:
    land = Land(**land_in.dict(), user=user)
    await land.insert()
    return land.id


@router.patch("/update/{land_id}")
async def update_land(user: GcauDep, land_id: PydanticObjectId, land_update: LandIn):
    land = await Land.find_one(Land.id == land_id, Land.user.id == user.id)
    if not land:
        raise land_not_found_exc
    land = land.copy(update=land_update.dict(exclude_unset=True))
    await land.save()
    return land.id


@router.delete("/delete/{land_id}")
async def delete_land(user: GcauDep, land_id: PydanticObjectId):
    land = await Land.find_one(Land.id == land_id, Land.user.id == user.id)
    if not land:
        raise land_not_found_exc
    await land.delete()
    return {"message": "successfully deleted land"}


@router.post("/crop-recommend")
async def crop_recommend(user: GcauDep, land_id: PydanticObjectId):
    land = await Land.find_one(Land.id == land_id, Land.user.id == user.id)
    if not (land.nitrogen and land.phosphorous and land.potassium and land.ph and land.rainfall and land.location.city):
        raise land_missing_details_exc

    predictor.crop_prediction(N=land.nitrogen, P=land.phosphorous, K=land.potassium,ph=land.ph, rainfall=land.rainfall, city=land.city)
    


