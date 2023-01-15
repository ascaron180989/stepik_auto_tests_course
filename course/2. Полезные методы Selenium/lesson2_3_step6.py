from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin


def calc(x):
    x = int(x)
    return str(log(abs(12 * sin(int(x)))))


url = 'http://suninjuly.github.io/redirect_accept.html'

with webdriver.Chrome() as driver_chrome:
    driver_chrome.get(url)

    button_1 = driver_chrome.find_element(By.CLASS_NAME, 'btn')
    button_1.click()

    tabs_browser_list = list(driver_chrome.window_handles)
    driver_chrome.switch_to.window(tabs_browser_list[1])

    x = driver_chrome.find_element(By.ID, 'input_value')
    answer = calc(x.text)

    input_text_answer = driver_chrome.find_element(By.ID, 'answer')
    input_text_answer.send_keys(answer)

    button_2 = driver_chrome.find_element(By.CLASS_NAME, 'btn')
    button_2.click()

    alert = driver_chrome.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
