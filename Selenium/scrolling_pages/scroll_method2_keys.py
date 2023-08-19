import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    tag_p = browser.find_element(By.TAG_NAME, 'input').send_keys(Keys.DOWN)
    time.sleep(10)