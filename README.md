## Table of Contents

- [Setup & Installation](#setup--installation)
- [Practice Test Site](#practice-test-site)
- [Web Driver](#web-driver)
  - [Web Driver Methods](#web-driver-methods)
- [X-Path](#x-path)
  - [Format](#format)
  - [Examples](#examples)
- [CSS](#css)
  - [Format](#format-1)
- [Find Elements](#find-elements)
  - [By Class](#by-class)
- [Interactions](#interactions)
  - [Click, Clear, Send Keys](#click-clear-send-keys)
- [Waits](#waits)
  - [Implicit Wait](#implicit-wait)
  - [Explicit Waits](#explicit-waits)
  - [Expected Conditions](#expected-conditions)
- [Find elements from shadow DOM](#find-elements-from-shadow-dom)
- [Switch To](#switch-to)
  - [IFrame Example](#iframe-example)
  - [Alert Example](#alert-example)
- [Select](#select)
  - [Example](#example)
- [PyTest](#pytest)
  - [Setup](#setup-1)
  - [How to Run Tests](#how-to-run-tests)
  - [How to write Tests](#how-to-write-tests)
  - [How to use Fixtures](#how-to-use-fixtures)
  - [How to Parameterize Fixtures](#how-to-parameterize-fixtures)

### Setup & Installation

Install the following

- [Visual Studio Code](https://code.visualstudio.com/)
- [Python Standalone installer](https://www.python.org/downloads/)
- [VS Code extension for python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Install Selenium](https://www.selenium.dev/documentation/webdriver/getting_started/install_library/)
- `python -m pip install selenium`

## Practice Test Site

- [https://vallarasu.in/test/](https://vallarasu.in/test/)

##  Web Driver

- Firefox
- Chrome
- Edge
- Safari
- Ie

```python
from selenium import webdriver

driver = webdriver.Firefox()    # Firefox
driver = webdriver.Chrome()     # Chrome
driver = webdriver.Edge()       # Edge
driver = webdriver.Safari()     # Safari
driver = webdriver.Ie()         # Internet Explorer
```

### Web Driver Methods
---

- close
- get
- quit
- refresh

``` python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://vallarasu.in/test/")        # load URL
driver.close()                                  # close current tab
driver.quit()                                   # quit browser
```

### X-Path
---

| Format                                                       | Example                                        |
|--------------------------------------------------------------|------------------------------------------------|
| `// tag-name`                                                | `//button`                                     |
| `// tag-name [ @attribute= 'value' ]`                        | `//button[@id='sign-in-btn']`                  |
| `// tag-name [ contains ( @attribute, 'partial-value' )]`    | `//button[contains(text(),'Sign')]`            |
| `// tag-name [ starts-with ( @attribute, 'partial-value' )]` | `//input[starts-with(@id, 'user')]`            |
| `// tag-name [ ends-with ( @attribute, 'partial-value' )]`   | `//a[ends-with(@href, '.pdf')]`                |
| `// tag-name [ text() = 'text displayed' ]`                  | `//button[text()='Sign in']`                   |
| `// tag-name [ contains(text(), 'partial-text' )]`           | `//span[contains(text(), 'Welcome')]`          |
| `// tag-name [@id='x']/parent::div`                          | `//span[@id='x']/parent::div`                  |
| `// tag-name/ancestor::tag-name`                             | `//td/ancestor::table`                         |
| `// tag-name/child::tag-name`                                | `//div/child::p`                               |
| `// tag-name/descendant::tag-name`                           | `//div/descendant::span`                       |
| `// tag-name[@attribute='value']/following-sibling::li`      | `//li[@id='item2']/following-sibling::li`      |
| `// tag-name/preceding-sibling::tag-name`                    | `//h3/preceding-sibling::h2`                   |
| `// tag-name[@type='text' and @name='email']`                | `//input[@type='text' and @name='email']`      |
| `// tag-name[@type='submit' or @aria-label='Go']`            | `//button[@type='submit' or @aria-label='Go']` |
| `// tag-name[@id='menu']/*`                                  | `//div[@id='menu']/*`                          |
| `// * [@aria-hidden='true']`                                 | `//*[@aria-hidden='true']`                     |
| `// tag-name [@attribute='value'] // tag-name`               | `//div[@id='container']//button`               |

### CSS
---

#### Format

| type                 | syntax                                | example                                            |
|----------------------|---------------------------------------|----------------------------------------------------|
| tag-name             | only name                             | `a`, `button`, `input`, `select`, `div`            |
| id                   | #id                                   | `#search-input`, `#email-input`, `#password-field` |
| class                | .class                                | `.btn`, `.button-primary`, `.side-bar`             |
| tag name & attribute | tag-name[attribute='attribute value'] | `button[aria-label='Sign In']`                     |
| id & attribute       | #id[attribute='attribute value']      | `#login[aria-label='Sign In']`                     |
| class & attribute    | .class[attribute='attribute value']   | `.primary-btn[aria-label='Sign In']`               |


### Find Elements
---

```python

from selenium.webdriver.common.by import By

driver.find_element(By.XPATH, "//*[@data-testid='login-button']")
driver.find_elements(By.XPATH, "//button")

```

#### By Class

- ID = "id"
- NAME = "name"
- XPATH = "xpath"
- LINK_TEXT = "link text"
- PARTIAL_LINK_TEXT = "partial link text"
- TAG_NAME = "tag name"
- CLASS_NAME = "class name"
- CSS_SELECTOR = "css selector"

```python
driver.find_element(By.ID, "id")
driver.find_element(By.NAME, "name")
driver.find_element(By.XPATH, "xpath")
driver.find_element(By.LINK_TEXT, "link text")
driver.find_element(By.PARTIAL_LINK_TEXT, "partial link text")
driver.find_element(By.TAG_NAME, "tag name")
driver.find_element(By.CLASS_NAME, "class name")
driver.find_element(By.CSS_SELECTOR, "css selector")
```

### Interactions
---

- Click
- Send Keys
- Clear

#### Click, Clear, Send Keys

```python
user_name = driver.find_element(By.XPATH, "//*[@data-testid='user-name']")
user_name.clear()
user_name.send_keys("user@email.com")

user_name = driver.find_element(By.XPATH, "//*[@data-testid='user-pwd']")
user_name.send_keys("P@SSW0RD!")

login = driver.find_element(By.XPATH, "//*[@data-testid='login-button']")
login.click()
```

### Waits
---

- Implicit
- Explicit

#### Implicit Wait

```python

driver.implicitly_wait(2)
```

#### Explicit Waits


```python
from selenium.webdriver.support.wait import WebDriverWait

wait = WebDriverWait(driver, timeout=2)
wait.until(lambda _ : revealed.is_displayed())
```

#### Expected Conditions

expected_conditions (imported as EC) is a important module that provides conditions for explicit waits. 
Used together with WebDriverWait to make tests more stable

- `presence_of_element_located`
- `visibility_of_element_located`
- `element_to_be_clickable`
- `text_to_be_present_in_element`
- `title_is` / `title_contains`
- `url_to_be` / `url_contains` 
- `alert_is_present`
- `invisibility_of_element_located`

```python

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

wait = WebDriverWait(driver, timeout=2)
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@data-testid='user-name']")))

user_name = driver.find_element(By.XPATH, "//*[@data-testid='user-name']")
user_name.send_keys("user@email.com")
```

Wait for any of (at least one) given conditions to be true 

```python
wait.until(EC.any_of(
        EC.text_to_be_present_in_element((By.ID, "status"), "Success"),
        EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
        ))
```

### Find elements from shadow DOM

Shadow DOM is a browser feature that renders parts of the DOM tree inside a "shadow root". 
This makes web components modular and prevents style leakage or accidental access from outside.

In Selenium elements inside Shadow DOM are not reachable with normal find_element() calls, they live in a separate subtree.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://vallarasu.in/test/shadow-dom.html")

# 1. Find the shadow host (the custom element that owns the shadow DOM)
shadow_host = driver.find_element(By.XPATH, "//div[@id='dob-container']")

# 2. Get the shadow root (this is the key line!)
shadow_root = shadow_host.shadow_root

# AFTER SHADOW ROOT ONLY USE BASIC CSS SELECTORS, ID, CLASS, NAME, CSS SELECTORS

# 3. Now search INSIDE the shadow DOM — like a mini-driver
inside_element = shadow_root.find_element(By.ID, "dob_day")
print(inside_element.text)

driver.quit()
```

### Switch To
---

Methods that help from switching from one context to another, for example, tabs, windows, frames and alert windows.

- `switch_to.window`
- `switch_to.frame(reference)`
- `switch_to.default_content()`
- `switch_to.alert()`
- `switch_to.active_element`
- `switch_to.parent_frame()`


#### IFrame Example:

```python
# option 1
driver.switch_to.frame("iframeResult")           # name or id attribute

# option 2
iframe_element = driver.find_element(By.ID, "iframe-element-id")
driver.switch_to.frame(iframe_element)

# switch back to main content
driver.switch_to.default_content()
```

#### Alert Example

```python

alert = driver.switch_to.alert

print("Alert text:", alert.text)

alert.accept()       # OK / Yes
# alert.dismiss()    # Cancel / No
# alert.send_keys("Hello from Selenium")
# alert.accept()
```

### Select
---

Select class enables interaction with Select / Drop Down UI element possible with following ways

- options
- select_by_index
- select_by_visible_text
- select_by_value

``` python
from selenium.webdriver.support.select import Select
```

#### Example

```python
driver = webdriver.Chrome(options)
driver.implicitly_wait(3)
driver.get("https://vallarasu.in/test/select")

# locate and create Select
ed = driver.find_element(By.ID, "education")
ed_select = Select(ed)

# options
print(len(ed_select.options))

# select an option
ed_select.select_by_index(1)
ed_select.select_by_visible_text("SSLC")
ed_select.select_by_value("4")
```

```python
assert ed_select.all_selected_options[0] == ed_select.options[3]
print(ed_select.all_selected_options[0].text)
```

## PyTest
---

PyTest framework allows to write, manage and run tests easily

### Setup

`python -m pip install pytest`

### How to Run Tests

- `pytest test_file.py`
- `pytest test_folder/`
- `pytest -k test_class_name`

### How to write Tests

Write functions as usual in python with test logic.
Just append test to the function name.

```python
def test_login_credentials_work():

        # test code here
        expected = "Login Success"
        actual = "Login Failed"

        # Assert
        assert actual == expected
```

```python
def test_validate_account_info():

        # test code here
        expected = "Login Success"
        actual = "Login Failed"

        # Assert
        assert actual == expected, "Failed to Validate Account info"
```

### How to use Fixtures

Fixtures are used to provide information to test function

```python
import pytest

@pytest.fixture
def login_credential():
        return "amin", "p@assw0rd123"

def test_login_works(login_credential):

        user, password = login_credential
        # test code here
```

```python
import pytest
from db import connect

@pytest.fixture(scope="session")
def db_connection():
        connection = connect()
        yield connection
        connection.close()
```

### How to Parameterize Fixtures

```python
import pytest

@pytest.mark.parametrize("user,password", [("admin", "pass123"), ("user", "p@assw0rd")])
def login_credential(user, password):

       # test code here
        expected = "Login Success"
        actual = "Login Failed"

        # Assert
        assert actual == expected, "Failed to Validate Login" 
```
