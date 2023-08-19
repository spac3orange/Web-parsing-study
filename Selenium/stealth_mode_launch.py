from selenium import webdriver
from selenium.webdriver.common.by import By

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)
    a = browser.find_element(By.TAG_NAME, 'a')
    print(a.get_attribute('href'))