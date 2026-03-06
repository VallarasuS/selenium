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

driver.get("www.selenium.dev")  # load URL
driver.close()                  # close current tab
driver.quit()                   # quit browser
```

### X-Path
---

#### FORMAT

- `// tag-name [ @attribute-name = 'attribute-value' ]`
- `// tag-name [contains ( @attribute-name, 'partial' )]`

### Examples

- `//*[@data-testid='login-button']`
- `//button[@id='submit' or @name='submit']`
- `//button[text()='Sign in']`
- `//button[contains(text(),'Sign')]`
- `//button[contains(@class,'btn-primary')]`
- `//div[contains(@class,'modal')]//button[1]`
- `//label[text()='Email']/following-sibling::input`
- `//tr[td='John']//button[contains(text(),'Edit')]`


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

