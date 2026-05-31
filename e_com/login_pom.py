from selenium import webdriver
from selenium.webdriver.common.by import By

from home_pom import HomePOM

class LoginPOM:

    def __init__(self, driver):

        self.url = "https://vallarasus.github.io/e-com/login.html"
        self.user_name_locator = "//input[@id='auth-user']"
        self.password_locator = "//input[@data-testid='auth-pass']"
        self.login_btn_locator = "//button[text()='Login']"
        self.driver = driver

    def login(self, user, password):

        self.driver.get(self.url)

        self.title = self.driver.current_url

        user_element = self.driver.find_element(By.XPATH, self.user_name_locator)
        pass_element = self.driver.find_element(By.XPATH, self.password_locator)
        login_btn_element = self.driver.find_element(By.XPATH, self.login_btn_locator)

        user_element.send_keys(user)
        pass_element.send_keys(password)
        login_btn_element.click()

        return HomePOM(self.driver)



    def forgot_password():
        pass

    def create_account():
        pass