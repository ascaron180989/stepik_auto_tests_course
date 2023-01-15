from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

url = 'http://suninjuly.github.io/file_input.html'
file_name = input('Введите имя прикрепляемого файла: ')
path = os.path.abspath(os.path.dirname(__file__))

with webdriver.Chrome() as driver_chrome:
    driver_chrome.get(url)

    input_text_firstname = driver_chrome.find_element(By.NAME, 'firstname')
    input_text_firstname.send_keys('Vyacheslav')

    input_text_lastname = driver_chrome.find_element(By.NAME, 'lastname')
    input_text_lastname.send_keys('Ershov')

    input_text_email = driver_chrome.find_element(By.NAME, 'email')
    input_text_email.send_keys('test@bk.ru')

    input_file = driver_chrome.find_element(By.NAME, 'file')
    send_file = os.path.join(path, file_name)
    input_file.send_keys(send_file)

    button = driver_chrome.find_element(By.CLASS_NAME, 'btn')
    button.click()

    sleep(10)