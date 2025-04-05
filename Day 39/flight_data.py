import requests
from data_manager import DataManager
from dotenv import load_dotenv
import os

load_dotenv()

DEFAULT_URL = "https://test.api.amadeus.com/v1"
TOKEN_URL = f"{DEFAULT_URL}/security/oauth2/token"
CITY_URL = f"{DEFAULT_URL}/reference-data/locations/cities"
API_KEY = os.getenv("FLIGHT_API_KEY")
API_SECRET = os.getenv("FLIGHT_API_SECRET")
token_params = {
    "grant_type": "client_credentials",
    "client_id": API_KEY,
    "client_secret": API_SECRET,

}
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.response = requests.post(TOKEN_URL, data=token_params, headers=headers)
        self.response.raise_for_status()
        self.authentication = self.response.json()['access_token']
        self.city_code()

    def city_code(self):
        data_manager = DataManager()
        city_list = data_manager.city_list
        headers = {
            "Authorization": "Bearer " + f"{self.authentication}"
        }
        for i, city in enumerate(city_list):
            params = {
                "keyword": {city.title()}
            }
            response = requests.get(CITY_URL, params=params, headers=headers)
            response.raise_for_status()
            iata_code = response.json()['data'][0]['iataCode']
            data_manager.sheety_update(iata_code, i)

