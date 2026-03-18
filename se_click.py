from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

# create driver and configure wait time
driver = webdriver.Chrome()
driver.implicitly_wait(3)

# open url
driver.get("https://vallarasu.in/test/drag-drop.html")
element = driver.find_element(By.XPATH, "//li//span[text()='John Adam']")

actions = ActionChains(driver)

actions.move_to_element(element).perform()
actions.click_and_hold(element).perform()
actions.context_click(element).perform()
actions.double_click(element).perform()
