from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

GOOGLE_SHEET = 'https://forms.gle/4ktSMfkYt2E6obZt9'
ZILLOW = 'https://appbrewery.github.io/Zillow-Clone/'
HEADERS = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
}
# extract data from Zillow website

response = requests.get(ZILLOW, headers=HEADERS)
website_html = response.text

soup = BeautifulSoup(website_html,'html.parser')

all_address = soup.select(selector='ul li address')
all_price = soup.select(selector='ul li div.PropertyCardWrapper span')
all_link = soup.select(selector='ul li div.StyledPropertyCardDataWrapper a')

address = [address.getText().strip() for address in all_address]
prices = [price.getText().split("/")[0].split("+")[0] for price in all_price]
links = [link.get('href') for link in all_link]

# Selenium set up

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(GOOGLE_SHEET)

# Filling form
for n in range(len(address)):
    time.sleep(3)
    address_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(f'{address[n]}')
    price_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(f'{prices[n]}')
    link_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(f'{links[n]}')
    submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()
    time.sleep(3)

    # submit another form
    submit_again = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_again.click()

driver.quit()
