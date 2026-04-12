from selenium import webdriver
from selenium.webdriver.common.by import By

# Arrange
url =  "https://www.selenium.dev/"
search_locator = "docsearch-1"

driver = webdriver.Firefox()
driver.get(url)

# Act
search_element = driver.find_element(By.ID, search_locator)
search_element.click()

# Assert
assert driver.title == "Selenium"