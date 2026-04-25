


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

def test_dob_dates():

    driver = webdriver.Firefox()
    driver.get("https://vallarasu.in/test/select")

    # Arrange
    day_locator = "//select[@id='dob_day']"
    month_locator = "//select[@id='dob_month']"
    year_locator = "//select[@id='dob_year']"

    day_el = driver.find_element(By.XPATH, day_locator)
    month_el = driver.find_element(By.XPATH, month_locator)
    year_el = driver.find_element(By.XPATH, year_locator)

    # Act
    day_select = Select(day_el)
    size_of_days = len(day_select.options)

    month_select = Select(month_el)
    size_of_months = len(month_select.options)

    day_select.select_by_visible_text("02")
    month_select.select_by_visible_text("03")

    # Assert
    assert size_of_days == 31
    assert size_of_months == 12

    # list comprehension
    selected_days = [o.text for o in day_select.all_selected_options]
    selected_months = []

    # simple for iteration
    for m in month_select.all_selected_options:
        selected_months.append(m.text)

    assert "02" in selected_days
    assert "03" in selected_months

    print(selected_days)
    print(selected_months)

    time.sleep(5)
    driver.quit()


test_dob_dates()


# numbers = [1, 2, 3, 4]
# print(numbers)

# str_numbers = [str(i) for i in numbers]
# # for i in numbers:
# #     str_numbers.append(str(i))

# print(str_numbers)

