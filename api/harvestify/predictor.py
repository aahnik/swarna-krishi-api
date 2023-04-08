# source: https://github.com/Gladiator07/Harvestify
# Credits: Atharva Ingle
# Gladiator07
#  GNU GENERAL PUBLIC LICENSE

from api.config import CONFIG
from api.harvestify.utils import fertilizer
from api import commons
import numpy as np
import requests


def weather_fetch(city_name, latitude=None, longitude=None):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    api_key = CONFIG.weather_api_key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    base_with_key = base_url + "appid=" + api_key
    if not (latitude and longitude):
        complete_url = base_with_key + "&q=" + city_name
    else:
        complete_url = base_with_key + f"&lat={latitude}&lon={longitude}"

    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] not in ("404", "401"):
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None


def crop_prediction(N, P, K, ph, rainfall, city):
    if weather_fetch(city) is not None:
        temperature, humidity = weather_fetch(city)
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        my_prediction = commons.crop_recommendation_model.predict(data)
        return my_prediction[0]
    else:
        return None


def fertilizer_recommend(N, P, K, crop_name):
    df = commons.fertilizer_df
    nr = df[df["Crop"] == crop_name]["N"].iloc[0]
    pr = df[df["Crop"] == crop_name]["P"].iloc[0]
    kr = df[df["Crop"] == crop_name]["K"].iloc[0]

    n = nr - N
    p = pr - P
    k = kr - K
    temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
    max_value = temp[max(temp.keys())]
    if max_value == "N":
        if n < 0:
            key = "NHigh"
        else:
            key = "Nlow"
    elif max_value == "P":
        if p < 0:
            key = "PHigh"
        else:
            key = "Plow"
    else:
        if k < 0:
            key = "KHigh"
        else:
            key = "Klow"

    return str(fertilizer.fertilizer_dic[key])
