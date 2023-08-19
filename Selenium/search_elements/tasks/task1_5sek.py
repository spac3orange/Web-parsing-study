import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/1/1.html'
text = ['Name', 'Surname', 'Sursurname', 'Age', 'City', 'EMAIL']

with webdriver.Chrome() as browser:
    browser.get(url)
    inputs = browser.find_elements(By.CLASS_NAME, 'form')
    button = browser.find_element(By.ID, 'btn')
    for i, item in enumerate(inputs):
        print(item.text)
        item.send_keys(text[i])
    button.click()
    time.sleep(50)