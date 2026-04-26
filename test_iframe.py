from selenium import webdriver
from selenium.webdriver.common.by import By

import time

def test_element_within_iframe():

    # Arrange
    driver = webdriver.Firefox()
    driver.implicitly_wait(2)

    driver.get("https://vallarasu.in/test/iframe")

    # element is present inside iframe
    # switch to iframe first, then locate elements

    frame = driver.find_element(By.XPATH, "//iframe[@data-test-id='iframe-form-container']")
    driver.switch_to.frame(frame)

    name_locator =  "//input[@placeholder='Full Name']"
    name_el = driver.find_element(By.XPATH, name_locator)

    # Act
    name_el.send_keys("Vallarasu")
    driver.switch_to.default_content()

    # Assert
    assert driver.title == "iFrame Form Fields Automation Testing"
    driver.quit()


if __name__ == "__main__":
    test_element_within_iframe()