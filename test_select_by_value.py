from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time

def test_select_by_value_example():

    driver = webdriver.Firefox()
    driver.get("https://vallarasu.in/test/select")

    # Arrange
    ed_locator = "//select[@id='education']"

    #Act
    ed_el = driver.find_element(By.XPATH, ed_locator)
    ed_select = Select(ed_el)
    ed_select.select_by_value("2")

    # Assert
    assert ed_select.first_selected_option.text == "Under Graduate (UG)"
    print(ed_select.first_selected_option.text)

    time.sleep(5)
    driver.quit()


test_select_by_value_example()