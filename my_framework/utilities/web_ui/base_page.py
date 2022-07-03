from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import click


class BasePage:

    def __init__(self, driver):
        self._driver = driver

    def wait_until_element_located(self, locator):
        return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.wait_until_element_located(locator)
        element.click()

    def send_keys(self, locator, value):
        element = self.wait_until_element_located(locator)
        element.send_keys(value)















