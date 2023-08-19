import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/3/3.html'

driver_options = webdriver.ChromeOptions()
driver_options.add_argument('--headless')

with webdriver.Chrome(options=driver_options) as browser:
    browser.get(url)
    elems = browser.find_elements(By.CSS_SELECTOR, 'p:nth-child(2)')
    summ = 0
    for i in elems:
        a = i.text.split('\n')
        for item in a:
            summ += int(item)
print(summ)