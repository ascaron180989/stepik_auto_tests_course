from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = 'http://suninjuly.github.io/registration1.html'
welcome_text = 'Congratulations! You have successfully registered!'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    input1.send_keys('Vyacheslav')

    input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    input2.send_keys('Ershov')

    input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    input3.send_keys('ascaron@bk.ru')

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

    sleep(1)

    w_text = browser.find_element(By.TAG_NAME, 'h1')
    w_text = w_text.text

    assert welcome_text == w_text

finally:
    browser.quit()