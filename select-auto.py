from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://vallarasu.in/test/select")

# locate DOB drop down by id
date = driver.find_element(By.ID, "dob_day")

# create Select object from element found
date_drop_down = Select(date)

# get all options
length = len(date_drop_down.options)
print(length)
assert length == 31

# change values
# - by text
# - by index
# - by value

education = driver.find_element(By.ID, "education")
ed_drop_down = Select(education)

length = len(ed_drop_down.options)
print(length)


time.sleep(3)

# Select By Index
# Zero based index
ed_drop_down.select_by_index(2)

time.sleep(3)

# Select By Value
ed_drop_down.select_by_value("5")

time.sleep(3)

# Select By Visible Text
ed_drop_down.select_by_visible_text("HSC")

time.sleep(3)
