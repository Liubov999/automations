from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from my_framework.utilities.web_ui.base_page import BasePage


class LoginModal(BasePage):
    __modal_login = (By.XPATH, "//div[@id ='popup-auth']")
    __email_input = (By.XPATH, "//input[@placeholder='Логін']")
    __password_input = (By.XPATH, "//input[@name='user_pw']")
    __login_button = (By.XPATH, "//span[text()='Увійти']")
    __header_user_page = (By.XPATH, "//h1[@class='page-header']")
    __forget_password_modal = (By.XPATH, "//div[@id='popup-forget-password']")
    __forget_button = (By.XPATH, "//div[@data-popup='popup-forget-password']")
    __close_forget_password_modal = (By.XPATH, "//div[@id='popup-forget-password']//div["
                                               "@class='simple-popup__layout']//div[@class='menu__close-button']")
    __close_login_modal = (By.XPATH, "//div[@id='popup-auth']//div[@class='simple-popup__layout']//div[@class='menu__close-button']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_modal_login(self):
        modal = self.__modal_login
        return modal

    def set_user_email(self, user_email):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.__email_input))
        self.send_keys(self.__email_input, user_email)

    def set_user_password(self, password):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.__password_input))
        self.send_keys(self.__password_input, password)

    def click_login_button(self):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.__login_button))
        self.click(self.__login_button)

    def get_user_page_header(self):
        header = self.wait_until_element_located(self.__header_user_page)
        return header

    def click_forget_button(self):
        self.click(self.__forget_button)

    def click_close_forget_button(self):
        self.click(self.__close_forget_password_modal)

    def click_close_login_button(self):
        self.click(self.__close_login_modal)

    def get_close_button_login_modal(self):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.__close_login_modal))
        return self

    def get_close_button_forget_password(self):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.__close_forget_password_modal))
        return self

    def get_forget_password_button(self):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.__forget_button))
        return self

    def get_forget_password_modal(self):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.__forget_password_modal))
        return self

