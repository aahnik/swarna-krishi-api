from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from api.config import CONFIG
from api.models.user import UserInDB
from api.models.crop import Crop


description = """
# Swarna Krishi API

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
    await init_beanie(database=db, document_models=[UserInDB, Crop])
