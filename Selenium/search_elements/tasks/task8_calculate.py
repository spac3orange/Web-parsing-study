import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/6/6.html'

# driver_options = webdriver.ChromeOptions()
# driver_options.add_argument('--headless')
summ = 0

with webdriver.Chrome() as browser:
    browser.get(url)
    elems = browser.find_element(By.ID, 'text_box').text
    result = str(eval(elems))
    get_list = browser.find_elements(By.TAG_NAME, 'option')
    for i in get_list:
        if i.text.strip() == result:
            i.click()
        else:
            continue
    btn = browser.find_element(By.ID, 'sendbutton').click()
    time.sleep(10)

