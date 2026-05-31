
from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePOM:

    def __init__(self, driver):
        self.driver = driver
        self.title = driver.title

    def select_category(self, category):
        
        cat_locator = "//label[text()='{0}']".format(category)
        cat_element = self.driver.find_element(By.XPATH, cat_locator)
        cat_element.click()

        self.url = self.driver.current_url