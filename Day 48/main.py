from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# set up the driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on
cookie = driver.find_element(By.ID, value="cookie")

# Get upgrade item ids.
items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

print(item_ids)

timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade prices
        prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        item_prices = []

        # Convert <b> to an integer
        for price in prices:
            element_text = price.text
            if element_text != "":
                item_prices.append(int(element_text.split("-")[1].strip().replace(",", "")))

        # Create dictionary for store items and prices
        cookie_upgrade = {}
        for n in range(len(item_prices)):
            cookie_upgrade[item_prices[n]] = item_ids[n]

        # Get current cookie count
        current_money = driver.find_element(By.ID, value="money").text
        if "," in current_money:
            current_money = current_money.replace(",", "")
        cookie_count = int(current_money)

        # Get affordable cookie
        affordable_upgrades = {}
        for cost, id in cookie_upgrade.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        driver.find_element(By.ID, value=affordable_upgrades[highest_price_affordable_upgrade]).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_sec = driver.find_element(By.ID, value="cps").text
        print(cookie_per_sec)
        break

# driver.quit()