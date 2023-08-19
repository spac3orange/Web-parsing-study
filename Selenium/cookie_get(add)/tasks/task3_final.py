import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/methods/5/index.html'
url_pattern = 'https://parsinger.ru/methods/5/'

# driver_options = webdriver.ChromeOptions()
# driver_options.add_argument('--headless')

exp_list = []
dct = {}
with webdriver.Chrome() as browser:
    browser.get(url)
    links = browser.find_elements(By.TAG_NAME, 'a')
    links_urls = [link.get_attribute('href') for link in links]

    for link in links_urls:
        # print(link.get_attribute('href'))
        url = link
        print(url)
        browser.get(url)
        ck = browser.get_cookies()
        print(ck)
        for cookie in ck:
            expiry = int(cookie['expiry'])
            dct[f'{link}'] = expiry
a = max(dct.values())
for k, v in dct.items():
    if v == a:
        with webdriver.Chrome() as browser:
            url = k
            print(k)
            browser.get(k)
            num = browser.find_element(By.ID, 'result').text
            print(num)
