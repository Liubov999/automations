from contextlib import suppress
import pytest
import allure
import request
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from my_framework.page_objects.home_page import HomePage
from tests_python.driver_factory import DriverFactory


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def create_driver(request):
    driver = DriverFactory.create_driver(driver_id=1, is_headless=False)
    driver.get("https://panama.ua/ua/")
    driver.maximize_window()
    WebDriverWait(driver, 10).until(EC.title_is(
        "Panama™ - найбільший дитячий інтернет-магазин у Києві та всій Україні | Більше 95000 дитячих товарів та "
        "іграшок у наявності"))
    yield driver
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.fixture()
def get_home_page(create_driver):
    return HomePage(create_driver)
