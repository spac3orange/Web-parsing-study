from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://ya.ru/')
    print(webdriver.get_cookie('_ym_uid')['expiry'])