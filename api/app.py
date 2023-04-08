from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from api.config import CONFIG
from api.models.user import UserInDB
from api.models.crop import Crop
from api.models.land import Land
from api import commons

description = """

Add crops by farmer

"""
app = FastAPI(title="Swarna Krishi API", version="0.0.1", description=description)


@app.get("/")
async def index() -> dict:
    return {"message": "server is up"}


@app.on_event("startup")
async def start_app():
    client = AsyncIOMotorClient(CONFIG.mongo_uri)
    db = client[CONFIG.db_name]
    await init_beanie(database=db, document_models=[UserInDB, Crop, Land])
    commons.crop_recommendation_model = commons.load_crop_recom_model()
    commons.fertilizer_df = commons.load_fertilizer_df()
