import requests
import os
from twilio.rest import Client

api_key = os.environ.get("OWN_API_KEY")  # environment variable
url = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


MY_LAT = -37.813629
MY_LON = 144.963058
COUNT = 4  # we only want 4 timestamp that cover only 12 hours from the time the scrip run
parameter = {
    "lat": MY_LAT,
    "lon": MY_LON,
    'cnt': COUNT,
    "appid": api_key,
}

response = requests.get(url, params=parameter)
response.raise_for_status()

data = response.json()['list']

for forecast in data:
    condition_code = forecast['weather'][0]['id']
    description = forecast['weather'][0]['description']

    if int(condition_code) < 700:
        client = Client(account_sid, auth_token)  # set up the client
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an ☔️ ",
            from_= os.environ.get("FROM_NUM"),
            to= os.environ.get("TO_NUM"),
        )

        print(message.status)

        break


