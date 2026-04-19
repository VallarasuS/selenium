from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Browser / Driver
    # - Create an instance / object or drive
    # interacting with it
        # - get
        # - close
        # - quit
        # - refresh
        # - maximize window

# Page
    # - title
    # - current_url 

# Elements
    # find_element
    # find_elements
        # click
        # clear
        # send_keys

def test_login_with_valid_credentials():
    # Arrange
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)

    driver.get("https://cs101.in/ecom/login.html")

    # //*[@id="auth-button"]
    # //*[@id="auth-button"]

    # //button[contains(text(), 'Next')]
    # //button[contains(@class, 'signup')]
    # //button[contains(@name, 'signup')]

    user_name_locator = "//input[@id='auth-user']"
    password_locator = "//input[@name='auth-pass']"
    login_button_locator = "//button[text()='Login']"

    user_name_el = driver.find_element(By.XPATH, user_name_locator)
    password_el = driver.find_element(By.XPATH, password_locator)
    login_btn_el = driver.find_element(By.XPATH, login_button_locator)

    # Act
    user_name_el.send_keys("admin")
    password_el.send_keys("admin")
    login_btn_el.click()

    # Assert
    assert driver.title == "NEO"
    assert driver.current_url == "https://cs101.in/ecom/index.html"
    driver.quit()


test_login_with_valid_credentials()