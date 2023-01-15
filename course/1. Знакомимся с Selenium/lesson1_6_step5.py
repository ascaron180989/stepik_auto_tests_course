from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

url = 'http://suninjuly.github.io/find_link_text'

with webdriver.Chrome() as driver_chrome:
    driver_chrome.get(url)

    link_locator = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = driver_chrome.find_element(By.LINK_TEXT, link_locator)
    link.click()

    input1 = driver_chrome.find_element(By.CSS_SELECTOR, 'form>div:nth-child(1)>input')
    input1.send_keys('Vyacheslav')

    input2 = driver_chrome.find_element(By.NAME, 'last_name')
    input2.send_keys('Ershov')

    input3 = driver_chrome.find_element(By.CLASS_NAME, 'city')
    input3.send_keys('Irkutsk')

    input4 = driver_chrome.find_element(By.ID, 'country')
    input4.send_keys('Russia')

    button = driver_chrome.find_element(By.CLASS_NAME, 'btn')
    button.click()

    sleep(10)