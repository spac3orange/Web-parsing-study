import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')

    list_input = []
    while True:
        input_tags = [x for x in browser.find_elements(By.TAG_NAME, 'input')]
        for tag_input in input_tags:
            if tag_input not in list_input:
                tag_input.send_keys(Keys.DOWN)
                tag_input.click()
                time.sleep(1)
                list_input.append(tag_input)