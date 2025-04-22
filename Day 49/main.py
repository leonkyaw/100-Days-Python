from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
PHONE = os.getenv("PHONE")


def abort_application():
    # Click close button
    close_button = driver.find_element(By.CSS_SELECTOR, value='div#artdeco-modal-outlet button')
    close_button.click()

    time.sleep(5)
    # Discard Application
    discard = driver.find_element(By.XPATH, value="/html/body/div[4]/div[2]/div/div[3]/button[1]")
    discard.click()

# set up the driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4196009906&distance=25&f_AL=true&geoId=100992797&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

# Signin_method
signin_method = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
signin_method.click()
time.sleep(3)

# Linkedin Login
email = driver.find_element(By.CSS_SELECTOR, value="input#base-sign-in-modal_session_key")
email.send_keys(EMAIL)
password = driver.find_element(By.CSS_SELECTOR, value="input#base-sign-in-modal_session_password")
password.send_keys(PASSWORD)
sign_in = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
sign_in.click()

# CAPTCHA - Solve Puzzle Manually
input("Press Enter when you have solved the Captcha")

# Get Listing
time.sleep(5)
all_listings = driver.find_elements(By.CSS_SELECTOR, value='main div ul li')

# Apply for Job
for listing in all_listings:
    listing.click()
    time.sleep(2)
    try:
        apply_job = driver.find_element(By.ID, value="jobs-apply-button-id")
        apply_job.click()

        # Filling application form
        time.sleep(5)
        mobile_number = driver.find_element(By.ID, value="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4204347025-17902276300-phoneNumber-nationalNumber")
        if mobile_number.text == "":
            mobile_number.send_keys(PHONE)

        # Check Submission Button
        next_button = driver.find_element(By.CSS_SELECTOR, value='footer button')
        if next_button.get_attribute("aria-label") == "Continue to next step":
            abort_application()
            continue
        else:
            # Click Submission Button
            next_button.click()
            time.sleep(3)

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
# driver.quit()

