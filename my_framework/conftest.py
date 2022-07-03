from selenium.webdriver.support import expected_conditions as EC


import pytest
from selenium.webdriver.support.wait import WebDriverWait
from my_framework.page_objects.home_page import HomePage
from tests_python.driver_factory import DriverFactory


@pytest.fixture()
def create_driver():
    driver = DriverFactory.create_driver(driver_id=1, is_headless=False)
    driver.get("https://panama.ua/ua/")
    driver.maximize_window()
    WebDriverWait(driver, 10).until(EC.title_is(
        "Panama™ - найбільший дитячий інтернет-магазин у Києві та всій Україні | Більше 95000 дитячих товарів та "
        "іграшок у наявності"))
    yield driver
    driver.quit()


@pytest.fixture()
def get_home_page(create_driver):
    return HomePage(create_driver)



    #assert header == login_modal_page.get_user_page_header(),\
           #f'\nUser not loginned\nActual:{header}\nExpected:{login_modal_page.get_user_page_header()}'