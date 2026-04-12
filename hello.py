# launch browser
# open url
# ensure page is loaded
# take action on an element on page
    # - key in search term
    # - click search

# launch browser

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Browser
# Arrange
driver = webdriver.Firefox()
driver.get("https://www.selenium.dev/")

# driver.get
# driver.find_element
# driver.find_elements 

time.sleep(5)

print(driver.title)
print(driver.current_url)

search_element = driver.find_element(By.ID, "docsearch-1")
search_element.click()

# search_element.send_keys
# search_element.click
# search_element.clear

time.sleep(5)


driver.quit()

# AAA


# Act

# Assert
