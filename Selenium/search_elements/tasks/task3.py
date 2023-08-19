import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.html'

driver_options = webdriver.ChromeOptions()
driver_options.add_argument('--headless')
with webdriver.Chrome(options=driver_options) as browser:
    browser.get(url)
    elems = browser.find_elements(By.CLASS_NAME, 'text')
    summ = 0
    for i in elems:
        a = i.text.split('\n')
        for item in a:
            summ += int(item)
print(summ)