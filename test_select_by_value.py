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
    # 1. locate the element using Xpath
    ed_el = driver.find_element(By.XPATH, ed_locator)

    # 2. Wrap / Create Select instance using element from previous step
    ed_select = Select(ed_el)

    #3. Choose an option by value / index / display text
    ed_select.select_by_value("2")

    # Assert

    # Validate values set in step #3 is applied
    assert ed_select.first_selected_option.text == "Under Graduate (UG)"
    print(ed_select.first_selected_option.text)

    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    test_select_by_value_example()