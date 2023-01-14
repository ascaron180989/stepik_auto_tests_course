from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = 'http://suninjuly.github.io/simple_form_find_task.html'

with webdriver.Chrome() as driver_chrome:
    driver_chrome.get(url)

    input1 = driver_chrome.find_element(By.TAG_NAME, 'input')
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