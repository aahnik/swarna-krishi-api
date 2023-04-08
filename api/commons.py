from api.config import CONFIG
import pandas as pd
import pickle


def load_crop_recom_model():
    with open(CONFIG.crop_recommendation_model_path, "rb") as file:
        crop_recommendation_model = pickle.load(file)

    return crop_recommendation_model


def load_fertilizer_df():
    return pd.read_csv(CONFIG.fertilizer_csv_path)


crop_recommendation_model = None
fertilizer_df = None
