from selenium import webdriver
import time

browser = webdriver.Chrome() # создаем обьект браузера и передаем название браузера

browser.get('http://parsinger.ru/html/watch/1/1_1.html') # вызываем метод get для перехода по ссылке
button = browser.find_element("id", "sale_button").click() # нажимаем на кнопку
time.sleep(10)