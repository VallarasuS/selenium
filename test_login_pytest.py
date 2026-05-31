from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import pytest


@pytest.fixture
def category():
    return "electronics"

@pytest.fixture
def product(category):
    return "laptop", category


@pytest.fixture
def credential():
    # file = open(r"C:\Users\Valla\Documents\GitHub\py-selenium\credential.csv", "r")
    # data = file.readline()
    # file.close()
    # [user_name, password] = data.split(",")
    # return (user_name, password)

    return "admin", "p@ss1234"


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

    # credential = credential()
    user_name, password = credential
    prod, cat = product

    # Act
    user_el.send_keys(user_name)
    password_el.send_keys(password)

    time.sleep(5)

    login_button.click()

    # Assert
    assert driver.current_url != "Login Auth Automation Testing"
    driver.quit()


def test_order_works(credential, product):

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

    # credential = credential()
    user_name, password = credential

    # Act
    user_el.send_keys(user_name)
    password_el.send_keys(password)

    time.sleep(5)

    login_button.click()

    # Assert
    assert driver.current_url != "Login Auth Automation Testing"



@pytest.mark.parametrize("credential", [("admin", "admin"), ("admin", "pass"), ("admin", "1234") ])
def test_multiple_login(credential):
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

    # credential = credential()
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


# Py Test Scope

def add(x, y):
    return x + y

@pytest.fixture()
def values():
    # reading from file
    return [(1,2, 3), (-1,2,1), (-1,-2, -3)]

@pytest.fixture(scope="class")
def driver():
    firefox = webdriver.Firefox()
    return firefox

class TestAdd:

    def test_add_values(values):

        for params in values:
            validate_add(params)
        values.clear()


    def test_add_values_two (values):
        for params in values:
            validate_add(params)


    def validate_add(params):

        # Arrange
        x, y, expected = params

        # Act
        result = add(1, 2)

        # Assert
        assert result == 3

# Py Test Fixture Scope
    # function
    # class
    # 