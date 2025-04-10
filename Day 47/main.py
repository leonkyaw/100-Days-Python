import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

# AMAZON_URL = "https://appbrewery.github.io/instant_pot/"
LIVE_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
my_email = os.getenv("my_email")
password = os.getenv("password")
TARGET_PRICE = 100
# headers make the requests look less like a bot and sometimes the request might be cancelled if no headers
HEADERS = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "'Google Chrome';v='135', 'Not-A.Brand';v='8', 'Chromium';v='135'",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "macOS",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
}
response = requests.get(LIVE_URL, headers=HEADERS)
content = response.text

soup = BeautifulSoup(content, "lxml")
price = float(soup.find_all(class_="a-offscreen")[0].getText().strip("$"))
title = soup.find(id="productTitle").getText().strip()


if price < TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Amazon Price Alert!! \n\n{title} is now cost {price}\n{LIVE_URL}".encode("utf-8"))
