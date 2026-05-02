from selenium import webdriver
from selenium.webdriver.common.by import By

import time

def test_alert_window():

    # Arrange
    url = "https://vallarasu.in/test/alert"
    add_button_locator = "//input[@type='button' and @value='Add']"

    driver = webdriver.Firefox()
    driver.get(url)

    # Act
    add_button_el = driver.find_element(By.XPATH, add_button_locator)
    add_button_el.click()

    alert = driver.switch_to.alert
    print(alert.text)
    time.sleep(5)
    alert.accept()

    time.sleep(5)

    # Assert
    driver.quit()

test_alert_window()    