from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time


def test_shadow_dom_element():
    
    # Arrange
    driver = webdriver.Firefox()
    driver.get("https://vallarasu.in/test/shadow-dom.html")

    #host
    host_locator = "//div[@id='dob-container']"
    day_locator = "dob_day"

    # 1. find host
    host = driver.find_element(By.XPATH, host_locator)

    # 2. navigate to shadow_root
    shadow_root = host.shadow_root

    # 3. locate element within shadow root
    # NO XPATH
    day = shadow_root.find_element(By.ID, day_locator)
    day_select = Select(day)

    time.sleep(1)

    day_select.select_by_index(2)

    # Act
    driver.quit()


test_shadow_dom_element()