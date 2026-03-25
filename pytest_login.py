from selenium import webdriver
from selenium.webdriver.common.by import By

import time


def test_validate_login_credentials():

    # browser
    driver = webdriver.Chrome()
    driver.get("https://vallarasu.in/test/login")

    # page
    assert driver.title == "Login Auth Automation Testing"

    email = driver.find_element(By.ID, "login-user")
    password = driver.find_element(By.ID, "login-pass")

    email.send_keys("admin")
    password.send_keys("admin")

    time.sleep(5)

    button = driver.find_element(By.ID, "login-button")
    button.click()

    assert driver.current_url == "https://vallarasu.in/test/home.html?logged-in=1"


if __name__ == "__main__":
    test_validate_login_credentials()
