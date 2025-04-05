from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("twilio_account_sid")
auth_token = os.getenv("twilio_auth_token")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, price,depart, arrive, outbound_date, inbound_date):
        self.city = depart
        self.price = price
        self.arrive = arrive
        self.outbound_date = outbound_date
        self.inbound_date = inbound_date
        self.sending_message()

    def sending_message(self):
        client = Client(account_sid, auth_token)  # set up the client
        message = client.messages.create(
            body=f"Low price alert!Only {self.price} to fly from {self.city} to {self.arrive},"
                 f" on {self.outbound_date} until {self.inbound_date}.",
            from_=os.getenv("sender_num"),
            to=os.getenv("receiver_num")
        )
