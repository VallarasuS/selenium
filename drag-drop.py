from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

# create driver and configure wait time
driver = webdriver.Chrome()
driver.implicitly_wait(3)

# open url
driver.get("https://vallarasu.in/test/drag-drop.html")

# find drag and drop targets
drag = driver.find_element(By.XPATH, "//li//span[text()='John Adam']")
drop = driver.find_element(By.XPATH, "//ul[@id='selected-items']")

# perform drag and drop action
ActionChains(driver).drag_and_drop(drag, drop).perform()

time.sleep(10)
driver.quit()
