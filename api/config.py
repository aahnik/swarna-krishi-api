from decouple import config
from pydantic import BaseModel


class Settings(BaseModel):
    mongo_uri = config("MONGO_URI")
    salt = config("SALT").encode()
    secret_key = config("SECRET_KEY")
    algorithm = "HS256"
    access_token_expire_minutes = 120
    db_name = "krishi-db"
    weather_api_key = config("WEATHER_API_KEY")
    crop_recommendation_model_path = "ml-models/RandomForest.pkl"
    fertilizer_csv_path = "data/fertilizer.csv"


CONFIG = Settings()
