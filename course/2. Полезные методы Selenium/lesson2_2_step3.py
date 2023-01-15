from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

url = 'http://suninjuly.github.io/selects1.html'

with webdriver.Chrome() as driver_chrome:
    driver_chrome.get(url)

    num1 = driver_chrome.find_element(By.ID, 'num1').text
    num2 = driver_chrome.find_element(By.ID, 'num2').text
    answer = str(int(num1) + int(num2))

    select = Select(driver_chrome.find_element(By.CLASS_NAME, 'custom-select'))
    select.select_by_value(answer)

    button = driver_chrome.find_element(By.CLASS_NAME, 'btn')
    button.click()

    sleep(10)