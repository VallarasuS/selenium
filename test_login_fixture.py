from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest
import time

# AAA
# A - Arrange
# A - Act
# A - Assert


@pytest.fixture
def user_credential():
    file = open("credential.txt", "r")
    credentials = file.readline().split(",")
    file.close()
    return credentials


def test_validate_login_with_valid_credential(user_credential):  # "admin", "admin"

    # Arrange
    driver = webdriver.Chrome()
    driver.get("https://vallarasu.in/test/login")

    user_locator = "//input[@id='login-user']"
    pass_locator = "login-pass"
    login_locator = "login-button"
    expected_title = "Form Fields Automation Testing"

    user_value, password_value = user_credential  # "admin", "admin"

    # Act
    user = driver.find_element(By.XPATH, user_locator)
    password = driver.find_element(By.ID, pass_locator)
    login = driver.find_element(By.ID, login_locator)

    user.send_keys(user_value)
    password.send_keys(password_value)

    time.sleep(5)

    login.click()

    time.sleep(5)

    # Assert
    assert driver.title == expected_title
