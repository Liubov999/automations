import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_chrome(create_chrome_browser):
    driver_chrome = create_chrome_browser
    user_email = 'lubanya9999@gmail.com'
    user_password = 'kykyryky999'
    driver_chrome.get('https://panama.ua/ua/')
    button_enter_locator = "//div[@class='header__button enter']"
    button_enter_element = driver_chrome.find_element(By.XPATH, button_enter_locator)
    button_enter_element.click()
    email_input_locator = "//input[@name='user_login']"
    email_input_element = driver_chrome.find_element(By.XPATH, email_input_locator)
    email_input_element.send_keys(user_email)
    password_input_locator = "//input[@name='user_pw']"
    password_input_element = driver_chrome.find_element(By.XPATH, password_input_locator)
    password_input_element.send_keys(user_password)
    login_button_locator = "// button[ @ type = 'submit'] // span[text() = 'Увійти']"
    login_button_element = driver_chrome.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    current_title = driver_chrome.title
    assert current_title == driver_chrome.title, f'\nActual:{current_title}\nExpected:{driver_chrome.title}'


def test_login_firefox(create_firefox_browser):
    driver_firefox = create_firefox_browser
    user_email = 'lubanya9999@gmail.com'
    user_password = 'kykyryky999'
    driver_firefox.get('https://panama.ua/ua/')
    button_enter_locator = "//div[@class='header__button enter']"
    button_enter_element = driver_firefox.find_element(By.XPATH, button_enter_locator)
    button_enter_element.click()
    email_input_locator = "//input[@name='user_login']"
    time.sleep(2)
    email_input_element = driver_firefox.find_element(By.XPATH, email_input_locator)
    time.sleep(2)
    email_input_element.send_keys(user_email)
    time.sleep(2)
    password_input_locator = "//input[@name='user_pw']"
    password_input_element = driver_firefox.find_element(By.XPATH, password_input_locator)
    password_input_element.send_keys(user_password)
    login_button_locator = "// button[ @ type = 'submit'] // span[text() = 'Увійти']"
    login_button_element = driver_firefox.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    current_title = driver_firefox.title
    assert current_title == driver_firefox.title, f'\nActual:{current_title}\nExpected:{driver_firefox.title}'


def test_login_edge(create_edge_browser):
    driver_edge = create_edge_browser
    user_email = 'lubanya9999@gmail.com'
    user_password = 'kykyryky999'
    driver_edge.get('https://panama.ua/ua/')
    button_enter_locator = "//div[@class='header__button enter']"
    button_enter_element = driver_edge.find_element(By.XPATH, button_enter_locator)
    button_enter_element.click()
    email_input_locator = "//input[@name='user_login']"
    time.sleep(2)
    email_input_element = driver_edge.find_element(By.XPATH, email_input_locator)
    time.sleep(2)
    email_input_element.send_keys(user_email)
    time.sleep(2)
    password_input_locator = "//input[@name='user_pw']"
    password_input_element = driver_edge.find_element(By.XPATH, password_input_locator)
    password_input_element.send_keys(user_password)
    login_button_locator = "// button[ @ type = 'submit'] // span[text() = 'Увійти']"
    login_button_element = driver_edge.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    current_title = driver_edge.title
    assert current_title == driver_edge.title, f'\nActual:{current_title}\nExpected:{driver_edge.title}'
