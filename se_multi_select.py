from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time

# launch and open url

driver = webdriver.Chrome()
driver.get("https://vallarasu.in/test/multi-select")

# locate element by x-path
# //select[@id='language_select']

element = driver.find_element(By.XPATH, "//select[@id='language_select']")
language_select = Select(element)

size = len(language_select.options)

assert size == 6

# choose a language
language_select.select_by_visible_text("English")
assert language_select.all_selected_options[0].text == "English"

# //label[@id='languages_selected']

label = driver.find_element(By.XPATH, "//label[@id='languages_selected']")
assert label.text == "English"

# Select by visible text
language_select.select_by_visible_text("Tamil")

assert len(language_select.all_selected_options) == 2

# results = []
# for i in language_select.all_selected_options:
#     print(i.text)
#     results.append(i.text)

# list comprehension
results = [i.text for i in language_select.all_selected_options]

assert results.index("Tamil") > -1
assert results.index("English") > -1

time.sleep(10)
