import requests
from datetime import datetime
import os

GENDER = 'male'
WEIGHT_KG = 65
HEIGHT_CM = 174
AGE = 30


# Nutrition API
APP_USER = os.environ["APP_USER"]
API_KEY = os.environ["API_KEY"]
NUTRITIONIX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

parameters = {
    'query': input('Tell me which exercises you did: '),
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    'age': AGE,
}

headers = {
    "x-app-id": APP_USER,
    "x-app-key": API_KEY
}

response = requests.post(NUTRITIONIX_ENDPOINT, json=parameters, headers=headers)
data = response.json()


# Sheetly API to update google sheet
SHEETLY_ENDPOINT = os.environ["SHEETLY_ENDPOINT"]
TOKEN = os.environ["TOKEN"]

today = datetime.now()
auth = {
    "Authorization": "Basic " + str(TOKEN),
}
for item in data['exercises']:
    sheetly_data = {
        "sheet1": {
            "date": today.strftime("%d/%m/%Y"), # the column name is camel case "firstName" for First Name column
            "time": today.strftime("%X"),
            "exercise": item['name'].title(),
            "duration": item['duration_min'],
            "calories": item['nf_calories'],
        }
    }
    response_sheetly = requests.post(SHEETLY_ENDPOINT, json=sheetly_data, headers=auth)
    # or response_sheetly = requests.post(SHEETLY_ENDPOINT, json=sheetly_data, auth=(username, password))

    # Sheety Authentication Option 3: Bearer Token
    """
    bearer_headers = {
        "Authorization": f"Bearer {os.environ['ENV_SHEETY_TOKEN']}"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )    
    """
    print(f"Sheety Response: \n {response_sheetly.text}")
