from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

dictionary = {}
events = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')

for i, event in enumerate(events):
    place_holder = event.text.split("\n")
    dictionary.update({i: {'time': place_holder[0], 'name': place_holder[1]}})

print(dictionary)

# solution
# events_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
# events_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
# events = {}
#
# for n in range(len(events_times)):
#     events[n] = {
#         'time': events_times[n].text,
#         'name': events_names[n].text,
#     }
# print(events)

driver.quit()
