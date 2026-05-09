from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

import time

def test_key_combinations():

    # Arrange
    driver = webdriver.Firefox()
    driver.get("https://vallarasu.in/test/action-chain")

    input_locator = "//input[@id='name-input']"
    input_el = driver.find_element(By.XPATH, input_locator)

    time.sleep(5)

    # Act
    action = ActionChains(driver)
    # method chaining
    action.click(input_el).key_down(Keys.CONTROL).send_keys("A").key_down(Keys.DELETE).perform()
    actual = input_el.text
    expected = ""

    time.sleep(5)

    # Assert
    assert actual == expected, "Failed to clear text"
    driver.quit()


test_key_combinations()



