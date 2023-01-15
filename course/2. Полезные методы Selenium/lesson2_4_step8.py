from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin


def calc(x):
    x = int(x)
    return str(log(abs(12 * sin(int(x)))))


url = 'http://suninjuly.github.io/explicit_wait2.html'

with webdriver.Chrome() as driver_chrome:
    driver_chrome.get(url)
    wait = WebDriverWait(driver_chrome, 15)

    button_1 = driver_chrome.find_element(By.ID, 'book')
    if wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '100')):
        button_1.click()

    x = driver_chrome.find_element(By.ID, 'input_value')
    answer = calc(x.text)

    input_text_answer = driver_chrome.find_element(By.ID, 'answer')
    input_text_answer.send_keys(answer)

    button_2 = driver_chrome.find_element(By.ID, 'solve')
    button_2.click()

    alert = driver_chrome.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
