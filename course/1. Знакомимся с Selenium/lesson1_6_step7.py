from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = 'http://suninjuly.github.io/huge_form.html'

with webdriver.Chrome() as driver_chrome:
    driver_chrome.get(url)

    input_text_list = driver_chrome.find_elements(By.CSS_SELECTOR, '.first_block>input')
    for input_text in input_text_list:
        input_text.send_keys('Answer')

    button = driver_chrome.find_element(By.CLASS_NAME, 'btn')
    button.click()

    sleep(10)