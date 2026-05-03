from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import time

def double_click_increments_count():
    # Arrange
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.get("https://vallarasu.in/test/action-chain")

    count_locator = "//label[@id='click-count-label']"
    div_locator = "//div[@id='double-click-area']"
    div_el = driver.find_element(By.XPATH, div_locator)
    
    time.sleep(5)

    # Act
    actionChain = ActionChains(driver)
    actionChain.double_click(div_el).perform()

    time.sleep(5)

    count_el = driver.find_element(By.XPATH, count_locator)
    actual = count_el.text
    expected = "1"

    # Assert
    assert actual == expected
    driver.quit()

    
double_click_increments_count()



