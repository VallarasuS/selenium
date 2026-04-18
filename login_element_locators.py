from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def test_login_with_valid_credentials():
    # Arrange
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)

    driver.get("https://cs101.in/ecom/login.html")

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