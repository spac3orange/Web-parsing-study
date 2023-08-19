import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/2/2.html'

driver_options = webdriver.ChromeOptions()
driver_options.add_argument('--headless')

with webdriver.Chrome(options=driver_options) as browser:
    browser.get(url)
    inputs = browser.find_element(By.PARTIAL_LINK_TEXT, '16243162441624').click()
    res = browser.find_element(By.ID, 'result')
    print(res.text)
    time.sleep(10)