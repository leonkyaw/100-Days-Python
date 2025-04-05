#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Create an object of Class
data_manager = DataManager()
flight_data = FlightData()
flight_search = FlightSearch()

for n, code in enumerate(data_manager.iaia):
    flight_search.flight_search(code, n)
    notification_manager = NotificationManager(flight_search.price[n],
                                               flight_search.departure_airport_code[n],
                                               flight_search.arrival_airport_code[n],
                                               flight_search.outbound_date[n],
                                               flight_search.inbound_date[n])
