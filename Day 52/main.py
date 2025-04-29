from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from dotenv import load_dotenv
import os
import time

load_dotenv()

SIMILAR_ACCOUNT = 'chefsteps'
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach',True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        email = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        email.send_keys(USER_NAME)
        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        # Instagram asked to input the verification, this is the manual process
        input("Please click enter after putting the verification")

        # Check if there is any cookie warning
        decline_cookie_xpath = '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]'
        cookie_warning = self.driver.find_elements(By.XPATH, value=decline_cookie_xpath)

        if cookie_warning:
            cookie_warning[0].click()

        time.sleep(3)

        # Click "Not now" and ignore save-login info prompt
        save_login_prompt = self.driver.find_element(By.XPATH, value='//div[contains(text(), "Not now")]')
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(3)

        # Click "Not now" on notification prompt
        notifications_prompt = self.driver.find_element(By.XPATH, value='//div[contains(text(),"Not now")]')
        if notifications_prompt:
            notifications_prompt.click()

    def find_follower(self):
        time.sleep(5)

        # Show follower of the selected account.
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        time.sleep(3)
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(By.XPATH, modal_xpath)

        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as an HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        # Check and update the (CSS) Selector for the "Follow" buttons as required.
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(2)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, value="//button[contains(text(),'Cancel')]")
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_follower()
bot.follow()

