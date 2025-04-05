import requests
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_data import FlightData

FLIGHT_SEARCH = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    def __init_(self):
        self.flight_data = FlightData()
        self.data_manager = DataManager()
        self.price = []
        self.departure_airport_code = []
        self.arrival_airport_code = []
        self.outbound_date = []
        self.inbound_date = []
    #This class is responsible for talking to the Flight Search API.

    def flight_search(self, city, iteration):
        today = datetime.now()

        for period in range(1, 181):
            day = today + timedelta(period)
            return_day = day + timedelta(period + 8)

            params = {
                'originLocationCode': 'MEL',
                'destinationLocationCode': 'PAR',
                'departureDate': day.strftime("%Y-%m-%d"),
                'returnDate': return_day.strftime("%Y-%m-%d"),
                'adults': 1,
                'nonStop': 'true',
                'currencyCode': "AUD",

            }
            headers = {
                "Authorization": "Bearer " + f"{self.flight_data.authentication}"
            }
            response = requests.get(FLIGHT_SEARCH, params=params, headers=headers)
            response.raise_for_status()
            data = response.json()['data']
            price = 0

            try:
                price = data[0]['price']['total']
            except:
                price = 999999
            else:
                price = data[0]['price']['total']

            if int(price) <= self.data_manager.price_list[iteration]:
                self.price.append(price)
                self.departure_airport_code.append(data[0]["itineraries"][0]["segments"][0]["departure"]["iataCode"])
                self.departure_airport_code.append(data[0]["itineraries"][0]["segments"][0]["arrival"]["iataCode"])
                outbound_date = data[0]["itineraries"][0]["segments"][0]["departure"]["at"].split("T")
                inbound_date = data[0]["itineraries"][0]["segments"][0]["arrival"]["at"].split("T")
                self.outbound_date.append(outbound_date[0])
                self.inbound_date.append(inbound_date[0])
                break
            else:
                self.price.append("NA")
                self.departure_airport_code.append(city)
