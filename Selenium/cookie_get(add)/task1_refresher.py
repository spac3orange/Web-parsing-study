from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/methods/1/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    elem = browser.find_element(By.ID, 'result')
    while not elem.text.isdigit():
        browser.refresh()
        elem = browser.find_element(By.ID, 'result')
    print(elem.text)