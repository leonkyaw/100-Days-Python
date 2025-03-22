import requests
from twilio.rest import Client
import os

# STOCK API
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
STATE = 'us'
FUNCTION = 'TIME_SERIES_DAILY'

parameters = {
    'function': FUNCTION,
    'symbol': STOCK,
    'apikey': STOCK_API_KEY,
}

# NEW API
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
parameters1 = {
    'qInTitle': COMPANY_NAME,
    'apiKey': NEWS_API_KEY,
}

# MESSAGE
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("AUTH_TOKEN")

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get('https://www.alphavantage.co/query', params=parameters)
response.raise_for_status()
data = response.json()
data_list = [value for (key, value) in data.items()]

ytd_price = float(data_list[0]['4. close'])
before_ytd_price = float(data_list[1]['4. close'])
change_in_price = (ytd_price - before_ytd_price)/before_ytd_price
percentage_change_in_price = round(abs(change_in_price)*100, 0)
up_down = None
if change_in_price > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if abs(change_in_price) > 0.05:
    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_response = requests.get('https://newsapi.org/v2/everything', params=parameters1)
    news_response.raise_for_status()
    articles = news_response.json()
    three_articles = articles['articles'][:3]
    formatted_article = [f"Headlines: {article['title']}. \nBrief: {article['description']}"
                         for article in three_articles]

    # STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    # set up the client
    client = Client(account_sid, auth_token)
    for article in formatted_article:
        message = client.messages.create(
            body=f"{STOCK}:{up_down}{percentage_change_in_price}%\n{article}",
            from_=os.envrion.get("SENDER_NUM"),
            to=os.envrion.get("RECEIVER_NUM"))

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
