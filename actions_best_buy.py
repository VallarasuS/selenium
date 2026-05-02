from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time

def locators_xpath_find_bestbuy():

    driver = webdriver.Firefox()
    driver.implicitly_wait(5)

    driver.get("https://www.bestbuy.com/site/misc/deal-of-the-day/pcmcat248000050016.c?id=pcmcat248000050016")
    driver.maximize_window()

    time.sleep(5)

    # ------------------------------
    if driver.title.find("Select your Country") > 1:
        driver.find_element(By.XPATH, "//h4[text()='United States']").click()
    # ------------------------------

    email_loc = "//form[@id='marketingCommunicationId-e9f43e57-bd5b-4a1a-8483-0a93a74b409a']//input[@id='input-e9f43e57-bd5b-4a1a-8483-0a93a74b409a']"
    email_el = driver.find_element(By.XPATH,email_loc)

    actions = ActionChains(driver)
    actions.scroll_to_element(email_el)

    time.sleep(5)

    email_el.send_keys("johnadam@gmail.com")

    time.sleep(5)

    signup_loc = "//form[@id='marketingCommunicationId-e9f43e57-bd5b-4a1a-8483-0a93a74b409a']//input[@title='Sign up']"
    signup_el = driver.find_element(By.XPATH,signup_loc)
    signup_el.click()

    # db_click_action = ActionChains(driver)
    # db_click_action.double_click(signup_el).perform()


locators_xpath_find_bestbuy()