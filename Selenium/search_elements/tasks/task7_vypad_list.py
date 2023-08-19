import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/7/7.html'

# driver_options = webdriver.ChromeOptions()
# driver_options.add_argument('--headless')
summ = 0

with webdriver.Chrome() as browser:
    browser.get(url)
    elems = browser.find_elements(By.TAG_NAME, 'option')
    for i in elems:
        print(i.text)
        summ += int(i.text)
    get_num = browser.find_element(By.ID, 'input_result').send_keys(summ)
    btn = browser.find_element(By.ID, 'sendbutton').click()
    time.sleep(10)

