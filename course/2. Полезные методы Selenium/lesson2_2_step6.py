from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin
from time import sleep


def calc(x):
    x = int(x)
    return str(log(abs(12 * sin(int(x)))))


url = 'http://suninjuly.github.io/execute_script.html'

with webdriver.Chrome() as driver_chrome:
    driver_chrome.get(url)

    x = driver_chrome.find_element(By.ID, 'input_value')
    scrolling = x.location_once_scrolled_into_view
    answer = calc(x.text)

    input_text = driver_chrome.find_element(By.ID, 'answer')
    input_text.send_keys(answer)

    input_checkbox = driver_chrome.find_element(By.ID, 'robotCheckbox')
    input_checkbox.click()

    input_radiobutton = driver_chrome.find_element(By.ID, 'robotsRule')
    input_radiobutton.click()

    button = driver_chrome.find_element(By.CLASS_NAME, 'btn')
    button.click()

    sleep(10)

