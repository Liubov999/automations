
from selenium.webdriver.support import expected_conditions as EC
import pytest

from my_framework.page_objects.login_modal import LoginModal
from my_framework.utilities.driver_factory import DriverFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure
from my_framework.utilities.web_ui.base_page import BasePage


class DeliveryPage(BasePage):

    __delivery_page_header = (By.XPATH, "//h1")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step
    def get_delivery_page_header(self):
        header = self.wait_until_element_located(self.__delivery_page_header)
        return header
