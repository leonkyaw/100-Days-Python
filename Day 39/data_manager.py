import requests
from dotenv import load_dotenv
import os

load_dotenv()
SHEETY_GET = os.getenv('SHEETY_GET')
SHEETY_PUT = os.getenv('SHEETY_PUT')
AUTH_KEY = os.getenv("SHEETY_AUTH_KEY")
HEADER = {
    "Authorization": "Basic " + AUTH_KEY
}
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = requests.get(SHEETY_GET, headers= HEADER)
        self.response.raise_for_status()
        self.data = self.response.json()['prices']
        self.city_list = [city['city'] for city in self.data]
        self.price_list = [price['targetPrice'] for price in self.data]
        self.iaia = [price['iaiaCode'] for price in self.data]

    def sheety_update(self, iaia_code, iteration):
        params = {'price': {
            "iataCode": iaia_code
        }
        }
        url = SHEETY_PUT + f"/{iteration+2}"
        response = requests.put(url, json=params, headers=HEADER)
        response.raise_for_status()
