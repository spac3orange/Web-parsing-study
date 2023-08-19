import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/4/4.html'

# driver_options = webdriver.ChromeOptions()
# driver_options.add_argument('--headless')


with webdriver.Chrome() as browser:
    browser.get(url)
    elems = browser.find_elements(By.CLASS_NAME, 'check')
    for i in elems:
        i.click()

    buttn = browser.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(1)
    number = browser.find_element(By.ID, 'result')
    print(number.text)
