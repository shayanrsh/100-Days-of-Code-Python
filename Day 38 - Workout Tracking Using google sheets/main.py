import requests
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json",
}

user_input = input("Tell me which exercise you did: ")

user_exercise_params = {
    "query": user_input,
    "gender": "male",
    "weight_kg": 110,
    "height_cm": 184,
    "age": 26
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=user_exercise_params, headers=HEADERS)
result = response.json()

sheet_endpoint = os.environ.get("SHEET_ENDPOINT")

bearer_headers = {
    "Authorization": f"Bearer {os.environ.get('TOKEN')}"
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)
