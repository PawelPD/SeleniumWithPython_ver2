from time import sleep
from selenium.webdriver.common.by import By
from base.selenium_driver_helper import SeleniumDriverHelper
import utilities.custom_logger as cl
import logging


class LoginPage(SeleniumDriverHelper):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        #self.driver = driver - do usunięcia


    _login_link = (By.CSS_SELECTOR, ".user-info a")
    _email_field = (By.ID, "field-email")
    _password_field = (By.ID, "field-password")
    _login_button = (By.ID, "submit-login")
    _logout_button = (By.CSS_SELECTOR, ".user-info .logout")
    _login_failed_message = (By.XPATH, "//li[contains(text(),'Authentication failed.') "
                                       "or contains(text(),'Błąd uwierzytelniania.')]")

    def click_login_link(self):
        self.element_click(*LoginPage._login_link)

    def enter_email(self, email):
        self.send_keys(email, *LoginPage._email_field)

    def enter_password(self, password):
        self.send_keys(password, *LoginPage._password_field)

    def clear_email_field(self):
        self.clear_field(*LoginPage._email_field)

    def clear_password_field(self):
        self.clear_field(*LoginPage._password_field)

    def click_login_button(self):
        self.element_click(*LoginPage._login_button)

    def verify_login_successful(self):
        element = self.wait_for_element(*LoginPage._logout_button)
        result = self.is_element_present(element=element)
        return result

    def verify_login_failed(self):
        element = self.wait_for_element(*LoginPage._login_failed_message, timeout=3)
        result = self.is_element_present(element=element)
        return result

    def verify_login_title(self):
        result = self.verify_page_title("My account")
        if not result:
            result = self.verify_page_title("Moje konto")
        return result

    def login(self, email='default@Email', password='defaultPassword'):
        self.click_login_link()
        self.clear_email_field()
        self.clear_password_field()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def logout(self):
        self.element_click(*LoginPage._logout_button)
        self.wait_for_element(*LoginPage._login_link)
