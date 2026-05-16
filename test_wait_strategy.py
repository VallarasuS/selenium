# Explicit Wait
# how a fast a page renders

# wait for the page to load 
# implicit wait - fixed amount of time to wait
# keep wait time, increase time a test takes to complete

# Explicit Wait 

# WebDriverWait
# Different conditions to wait on

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def test_wait_strategy():

    # Arrange
    url = "https://vallarasu.in/test/wait"
    driver = webdriver.Firefox()
    driver.get(url)

    el_locator = "//a[contains(text(),'Tutorial')]"

    # Act
    wait = WebDriverWait(driver, timeout=60)
    el = wait.until(EC.visibility_of_element_located((By.XPATH, el_locator)))

    # Assert
    assert el.text == "Python Official Tutorial"
    driver.quit()

test_wait_strategy()