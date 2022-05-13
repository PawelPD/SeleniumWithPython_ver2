from selenium.webdriver import ActionChains, Keys
from base.selenium_driver_helper import SeleniumDriverHelper
from selenium.webdriver.common.by import By
import utilities.custom_logger as cl
import logging


class NavigationPage(SeleniumDriverHelper):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _main_page = (By.ID, "_desktop_logo")
    _category_clothes = (By.ID, "category-3")
    _category_clothes_men = (By.ID, "category-4")
    _category_clothes_women = (By.ID, "category-5")
    _category_accesories = (By.ID, "category-6")
    _category_accesories_stationery = (By.ID, "category-7")
    _category_accesories_home = (By.ID, "category-8")
    _category_art = (By.ID, "category-9")
    _language_dropdown = (By.ID, "_desktop_language_selector")
    _language_option_english = (By.CSS_SELECTOR, "#_desktop_language_selector .dropdown-item")[0]
    _language_option_polish = (By.CSS_SELECTOR, "#_desktop_language_selector .dropdown-item")[1]
    _search_field = (By.CSS_SELECTOR, ".ui-autocomplete-input")
    _logout = (By.CSS_SELECTOR, ".user-info .logout")
    _account = (By.CSS_SELECTOR, ".user-info .account")
    _cart = (By.CSS_SELECTOR, "_desktop_cart")
    _cart_number_of_items = (By.CSS_SELECTOR, "#_desktop_cart .cart-products-count")

    def go_to_main_page(self):
        self.element_click(*NavigationPage._main_page)

    def click_category_clothes(self):
        self.element_click(*NavigationPage._category_clothes)

    def click_category_clothes_men(self):
        drop_down = self.get_element(*NavigationPage._category_clothes)
        actions = ActionChains(self.driver)
        actions.move_to_element(drop_down)
        actions.perform()
        self.element_click(*NavigationPage._category_clothes_men)

    def click_category_clothes_women(self):
        drop_down = self.get_element(*NavigationPage._category_clothes)
        actions = ActionChains(self.driver)
        actions.move_to_element(drop_down)
        actions.perform()
        self.element_click(*NavigationPage._category_clothes_women)

    def click_category_accesories(self):
        self.element_click(*NavigationPage._category_accesories)

    def click_category_accesories_stationery(self):
        drop_down = self.get_element(*NavigationPage._category_accesories)
        actions = ActionChains(self.driver)
        actions.move_to_element(drop_down)
        actions.perform()
        self.element_click(*NavigationPage._category_accesories_stationery)

    def click_category_accesories_home(self):
        drop_down = self.get_element(*NavigationPage._category_accesories)
        actions = ActionChains(self.driver)
        actions.move_to_element(drop_down)
        actions.perform()
        self.element_click(*NavigationPage._category_accesories_home)

    def click_category_art(self):
        self.element_click(*NavigationPage._category_art)

    def change_language_to_polish(self):
        self.element_click(*NavigationPage._language_dropdown)
        self.element_click(*NavigationPage._language_option_polish)

    def change_language_to_english(self):
        self.element_click(*NavigationPage._language_dropdown)
        self.element_click(*NavigationPage._language_option_english)

    def enter_search_phrase(self, phrase):
        self.send_keys(phrase, *NavigationPage._search_field)
        self.send_keys(Keys.ENTER, *NavigationPage._search_field)

    def click_logout(self):
        self.element_click(*NavigationPage._logout)

    def click_account(self):
        self.element_click(*NavigationPage._account)

    def click_cart(self):
        self.element_click(*NavigationPage._cart)

    def get_cart_number_of_items(self):
        element = self.get_element(*NavigationPage._cart_number_of_items)
        number_of_items = element.text
        number_of_items = number_of_items.replace("(", "").replace(")", "")
        return number_of_items












