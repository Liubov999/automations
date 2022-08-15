from selenium.common import TimeoutException
import pytest
import allure


@allure.feature('Liubov Iarova')
def test_title(get_home_page):
    home_page = get_home_page
    current_title = get_home_page.get_current_title()
    assert current_title == get_home_page.get_current_title(), f'\nActual:{current_title}\nExpected:{get_home_page.get_current_title()} '


@allure.feature('Liubov Iarova')
def test_get_subscribe_element(get_home_page):
    home_page = get_home_page
    subscribe_element = get_home_page.get_subscribe_field
    assert subscribe_element == get_home_page.get_subscribe_field,\
        f'\nUnable to find element\nActual:{subscribe_element}\nExpected:{get_home_page.get_subscribe_field}'


@allure.feature('Storie_1')
@allure.feature('Liubov Iarova')
def test_subscribe(get_home_page):
    home_page = get_home_page
    email = 'test@test.com'
    get_home_page.set_user_email(email)
    get_home_page.click_subscribe()
    pop_up = get_home_page.subscribe_popup()
    assert pop_up,\
        f'\nPop Up is missing\nActual:{pop_up}\nExpected:{get_home_page.subscribe_popup()}'


@allure.feature('Liubov Iarova')
def test_login(get_home_page):
    user_email = 'lubanya9999@gmail.com'
    user_password = 'kykyryky999'
    home_page = get_home_page
    login_modal_page = home_page.click_sigh_in()
    login_modal_page.set_user_email(user_email)
    login_modal_page.set_user_password(user_password)
    login_modal_page.click_login_button()
    current_title = get_home_page.get_current_title()
    assert current_title == get_home_page.get_current_title(), f'\nActual:{current_title}\nExpected:{get_home_page.get_current_title()}'


@allure.feature('Storie_1')
@allure.feature('Liubov Iarova')
def test_forget_password_modal(get_home_page):
    home_page = get_home_page
    login_modal_page = home_page.click_sigh_in()
    login_modal_page.get_forget_password_button()
    login_modal_page.click_forget_button()
    modal = login_modal_page.get_forget_password_modal()
    assert modal == login_modal_page.get_forget_password_modal(),\
        f'\nUnable to find element\nActual:{modal}\nExpected:{login_modal_page.get_forget_password_modal()}'


@allure.feature('Liubov Iarova')
def test_close_login_modal(get_home_page):
    home_page = get_home_page
    login_modal_page = home_page.click_sigh_in()
    login_modal_page.get_close_button_login_modal()
    login_modal_page.click_close_login_button()


@allure.feature('Storie_2')
@allure.feature('Liubov Iarova')
def test_close_forgot_password_modal(get_home_page):
    home_page = get_home_page
    login_modal_page = home_page.click_sigh_in()
    login_modal_page.get_modal_login()
    login_modal_page.get_forget_password_button()
    login_modal_page.click_forget_button()
    login_modal_page.get_close_button_forget_password()
    login_modal_page.click_close_forget_button()


@allure.feature('Liubov Iarova')
def test_delivery(get_home_page):
    home_page = get_home_page
    delivery_page = home_page.click_delivery()
    header = delivery_page.get_delivery_page_header()
    assert header == delivery_page.get_delivery_page_header(), \
        f'\nUnable to find element\nActual:{header}\nExpected:{delivery_page.get_delivery_page_header()}'


@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_xfail_expected_failure():
    """this test is an xfail that will be marked as expected failure"""
    assert False


@allure.feature('Liubov Iarova')
def test_change_language(get_home_page):
    home_page = get_home_page
    get_home_page.click_ru()
    title_ru = get_home_page.get_title_ru()
    assert title_ru == get_home_page.get_title_ru(), f'\nActual:{title_ru}\nExpected:{get_home_page.get_title_ru()}'


@allure.feature('Liubov Iarova')
def test_call_back(get_home_page):
    home_page = get_home_page
    get_home_page.click_call_back()
    call_back = get_home_page.get_call_back_modal()
    assert call_back == get_home_page.get_call_back_modal(), f'\nActual:{call_back}\nExpected:{get_home_page.get_call_back_modal()}'

















