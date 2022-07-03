from selenium.webdriver.support import expected_conditions as EC
import pytest

from my_framework.page_objects.delivery_page import DeliveryPage
from my_framework.page_objects.login_modal import LoginModal
from my_framework.utilities.driver_factory import DriverFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from my_framework.utilities.web_ui.base_page import BasePage


class HomePage(BasePage):
    __sign_in_button = (By.XPATH, "//div[@class='header__button enter']")
    __input_subscribe_locator = (By.XPATH, "//input[@id='subscribe-input']")
    __subscribe_button = (By.XPATH, '//form[@id="footer-subscribe"]/button')
    __pop_up_window = (By.XPATH, '//div[@id="popup__window"]')
    __delivery_button = (By.XPATH, '//li[@class ="header__menu-item header-delivery"]//a[@href="/ua/delivery/"]')
    __current_title = (
        "Panama™ - найбільший дитячий інтернет-магазин у Києві та всій Україні | Більше 95000 дитячих товарів та "
        "іграшок у наявності")
    __lang_ru = (By.XPATH, "//a[@lang='ru']")
    __title_ru = ("Panama™ - самый детский интернет-магазин в Киеве и всей Украине | Более 95000 детских товаров и "
                  "игрушек в наличии")
    __call_back = (By.XPATH, '//div[@class="header__top"]//div[@data-popup="popup-callback"]')
    __call_back_modal = (By.XPATH, '//div[@id="popup-callback"]')

    def __init__(self, driver):
        super().__init__(driver)

    def get_current_title(self):
        current_title = WebDriverWait(self._driver, 10).until(EC.title_is(self.__current_title))
        return current_title

    def get_subscribe_field(self):
        subscribe_locator = self.wait_until_element_located(self.__input_subscribe_locator)
        return subscribe_locator

    def set_user_email(self, email):
        self.send_keys(self.__input_subscribe_locator, email)

    def click_subscribe(self):
        self.click(self.__subscribe_button)

    def subscribe_popup(self):
        pop_up = self.wait_until_element_located(self.__pop_up_window)
        return pop_up

    def click_sigh_in(self):
        self.click(self.__sign_in_button)
        return LoginModal(self._driver)

    def click_delivery(self):
        self.click(self.__delivery_button)
        return DeliveryPage(self._driver)

    def click_ru(self):
        self.click(self.__lang_ru)

    def get_title_ru(self):
        title_ru = WebDriverWait(self._driver, 10).until(EC.title_is(self.__title_ru))
        return title_ru

    def click_call_back(self):
        self.click(self.__call_back)

    def get_call_back_modal(self):
        call_back_modal = self.wait_until_element_located(self.__call_back_modal)
        return call_back_modal




