from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# AAA
# A - Arrange
# A - Act
# A - Assert


def test_validate_login_with_valid_credential():

    # Arrange
    driver = webdriver.Chrome()
    driver.get("https://vallarasu.in/test/login")

    user_locator = "//input[@id='login-user']"
    pass_locator = "login-pass"
    login_locator = "login-button"
    expected_title = "Form Fields Automation Testing"

    # Act
    user = driver.find_element(By.XPATH, user_locator)
    password = driver.find_element(By.ID, pass_locator)
    login = driver.find_element(By.ID, login_locator)

    user.send_keys("admin")
    password.send_keys("admin")
    login.click()

    # Assert
    assert driver.title == expected_title


def test_validate_login_with_invalid_credential():

    # Arrange
    driver = webdriver.Chrome()
    driver.get("https://vallarasu.in/test/login")

    user_locator = "//input[@id='login-user']"
    pass_locator = "login-pass"
    login_locator = "login-button"
    expected_title = "Form Fields Automation Testing"

    # Act
    user = driver.find_element(By.XPATH, user_locator)
    password = driver.find_element(By.ID, pass_locator)
    login = driver.find_element(By.ID, login_locator)

    user.send_keys("user123")
    password.send_keys("pass123")
    login.click()

    # Assert
    assert driver.title == expected_title
