from api.models.user import UserInDB
from api.models.land import Land


# intitializee beanie

async def send_weather_alerts():
    users = await UserInDB.find_all().list()
    for user in users:
        
