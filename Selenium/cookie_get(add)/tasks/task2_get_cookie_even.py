import time
from pprint import pprint
from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/3/index.html')
    values = webdriver.get_cookies()
    summ = 0
    for value in values:
        print(value)
        a = int(value['name'].split('_')[-1])
        if a % 2 == 0:
            summ += int(value['value'])
    time.sleep(5)
print(summ)