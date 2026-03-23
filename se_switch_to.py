from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# browser
driver = webdriver.Chrome()
driver.get("https://vallarasu.in/test/iframe")

frame = driver.find_element(By.XPATH, "//iframe[@src='./form.html']")
driver.switch_to.frame(frame)

name = driver.find_element(By.ID, "name-input")
name.send_keys("Selenium")

driver.switch_to.default_content()

time.sleep(5)
