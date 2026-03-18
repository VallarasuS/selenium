from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time

options = Options()
options.add_argument("--allow-file-access-from-files")

driver = webdriver.Chrome(options)
driver.implicitly_wait(3)
driver.get("https://vallarasu.in/test/select")

ed = driver.find_element(By.ID, "education")
ed_select = Select(ed)

print(len(ed_select.options))

ed_select.select_by_index(1)
ed_select.select_by_visible_text("SSLC")
ed_select.select_by_value("4")

assert ed_select.all_selected_options[0] == ed_select.options[3].text
print(ed_select.all_selected_options[0].text)

time.sleep(10)
