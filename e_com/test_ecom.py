from selenium import webdriver
import pytest

from login_pom import LoginPOM
from home_pom import HomePOM


@pytest.fixture(scope="session")
def firefox():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

# @pytest.fixture
# def login_pom(firefox):
#     loginPom = LoginPOM(firefox)
#     return loginPom

@pytest.fixture
def credential():

    # file = open("test.config.json","r")
    # cred = file.read()
    # return cred

    return "admin","admin"


def test_login_works_with_valid_cred(firefox, credential):
    
    # Arrange
    loginPom = LoginPOM(firefox)

    # Act
    user,password = credential
    homePOM = loginPom.login(user, password)

    # Assert 
    assert homePOM.title != "Neo - Login"


def test_place_order(firefox):
    
    # Arrange
    category = "Electronics"
    homePOM = HomePOM(firefox)

    # Act
    homePOM.select_category(category)

    # Assert
    assert homePOM.url.endswith(category.lower()) == True