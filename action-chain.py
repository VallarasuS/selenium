from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get("https://vallarasu.in/test/action-chain")


input_el = driver.find_element(By.XPATH, "//input[@id='name-input']")

action_one = ActionChains(driver)
action_one.click(input_el)
action_one.key_down(Keys.CONTROL)
action_one.send_keys("A")
action_one.key_down(Keys.DELETE)

action_one.perform()

time.sleep(3)

div_el = driver.find_element(By.XPATH, "//div[@id='double-click-area']")

db_click = ActionChains(driver)
db_click.double_click(div_el)
db_click.pause(2)
db_click.double_click(div_el)
db_click.pause(2)
db_click.double_click(div_el)
db_click.perform()

context_click_el = driver.find_element(By.XPATH, "//button[@class='context-menu-one']")

ctx_click = ActionChains(driver)
ctx_click.context_click(context_click_el)
ctx_click.click(
    driver.find_element(By.XPATH, "//li[contains(@class, 'context-menu-icon-copy')]")
)
ctx_click.perform()

time.sleep(2)

driver.switch_to.alert.accept()

time.sleep(2)

driver.switch_to.default_content()

link = driver.find_element(By.XPATH, "//a[@href='https://vallarasu.in/']")
a = ActionChains(driver)
a.key_down(Keys.CONTROL)
a.click(link)
a.perform()

time.sleep(10)
