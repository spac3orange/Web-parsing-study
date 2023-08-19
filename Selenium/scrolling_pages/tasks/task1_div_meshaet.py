import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/scroll/4/index.html'
values = []
with webdriver.Chrome() as webdriver:
    webdriver.get(url)
    elems = webdriver.find_elements(By.CLASS_NAME, 'btn')
    for elem in elems:

        webdriver.execute_script("return arguments[0].scrollIntoView(true);", elem)
        elem.click()
        values.append(int(webdriver.find_element(By.ID, 'result').text))
    time.sleep(5)


print(sum(values))