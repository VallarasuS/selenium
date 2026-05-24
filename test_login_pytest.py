from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import pytest


@pytest.fixture
def credential():
    file = open(r"C:\Users\Valla\Documents\GitHub\py-selenium\credential.csv", "r")
    data = file.readline()
    file.close()
    [user_name, password] = data.split(",")
    return (user_name, password)

# json

def test_login_works(credential):

    #  Arrange
    url = "https://vallarasu.in/test/login"
    user_locator = "//input[@id='login-user']"
    password_locator = "//input[@data-testid='login-pass']"
    login_locator = "login-button"

    driver = webdriver.Firefox()
    driver.get(url)

    user_el = driver.find_element(By.XPATH, user_locator)
    password_el = driver.find_element(By.XPATH, password_locator)
    login_button = driver.find_element(By.ID, login_locator)

    # credential = get_credentials()
    user_name, password = credential

    # Act
    user_el.send_keys(user_name)
    password_el.send_keys(password)

    time.sleep(5)

    login_button.click()

    # Assert
    assert driver.current_url != "Login Auth Automation Testing"
    driver.quit()

if __name__ == "__main__":
    test_login_works()