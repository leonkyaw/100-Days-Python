import requests
from datetime import datetime
import time
import smtplib
import os

my_email = 'leonpython4@gmail.com'  # my email
password = os.environ.get("PASSWORD")
MY_LAT = -37.8136291 # Your latitude
MY_LONG = 144.963058 # Your longitude
PARAMETERS = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def location_check():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - iss_latitude == abs(5) and MY_LONG - iss_longitude == abs(5):
        return True
    else:
        return False


def time_check():
    response = requests.get("https://api.sunrise-sunset.org/json", params=PARAMETERS)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.hour

    if current_hour >= sunset or current_hour <= sunrise:
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


while True:
    time.sleep(3)
    if location_check() and time_check():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg="Subject:Look Up!!\n\nThe ISS is just above your head. Time to drop your phone")


