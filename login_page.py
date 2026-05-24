# POM - Page Object Model
# every page has it's own class
# use the instance of this POM to invoke actions

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    user_name_locator = ""
    password_locator = ""

    def login(self):
        pass

    def forgot_password(self):
        pass

    def sign_up(self):
        pass