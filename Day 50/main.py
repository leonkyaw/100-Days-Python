from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from dotenv import load_dotenv
import time
import os

load_dotenv()

URL = "https://tinder.com/"
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")

# Set up the driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Login
time.sleep(5)
log_in = driver.find_element(By.XPATH, value='//*[@id="s67002758"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a')
log_in.click()

time.sleep(2)
login_option = driver.find_element(By.XPATH, value='//*[@id="s-1661378318"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]')
login_option.click()

# two window opened
time.sleep(2)
tinder = driver.window_handles[0]
facebook = driver.window_handles[1]
driver.switch_to.window(facebook)  # switch current window to the pop-up facebook window
print(driver.title)

# Facebook Login
fb_login = driver.find_element(By.NAME, value="email")
fb_login.send_keys(USER_NAME)
fb_pass = driver.find_element(By.NAME, value="pass")
fb_pass.send_keys(PASSWORD)
fb_pass.send_keys(Keys.ENTER)

#  security check
input("Please input enter after manual verification")

# to confirm the login
time.sleep(3)
login_confirmation = driver.find_element(By.XPATH, value='//*[@id="mount_0_0_6g"]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div')
login_confirmation.click()

# reverse main focus back to tinder
time.sleep(3)
driver.switch_to.window(tinder)

# Allow location
location = driver.find_element(By.XPATH, value='//*[@id="s-1661378318"]/div/div[1]/div/div/div[3]/button[1]')
location.click()

# Disallow notification
notification = driver.find_element(By.XPATH, value='//*[@id="s-1661378318"]/div/div[1]/div/div/div[3]/button[2]')
notification.click()

# Allow cookie
cookies = driver.find_element(By.XPATH, value='//*[@id="s67002758"]/div/div[2]/div/div/div[1]/div[1]/button')
cookies.click()

for n in range(100):

    # add a break between like
    time.sleep(2)

    try:
        like_button = driver.find_element(By.XPATH, value='//*[@id="main-content"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[4]/button')
        like_button.click()
    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button: .
    except ElementClickInterceptedException:  # like button run on the background and case this exception
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value='.itsAMatch a')
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)

driver.quit()  # exit the app after running out of like
