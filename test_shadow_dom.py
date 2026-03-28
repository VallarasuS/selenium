from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time


def test_validate_date_dropdown():
    # AAA

    # Arrange
    driver = webdriver.Chrome()
    driver.get("https://vallarasu.in/test/shadow-dom.html")

    host_locator = "//div[@id='dob-container']"
    dob_locator = "dob_day"

    # Act
    host_el = driver.find_element(By.XPATH, host_locator)
    shadow_root = host_el.shadow_root
    dob_el = shadow_root.find_element(By.ID, dob_locator)
    dob_select = Select(dob_el)

    # Assert
    assert len(dob_select.options) == 31

    time.sleep(5)
