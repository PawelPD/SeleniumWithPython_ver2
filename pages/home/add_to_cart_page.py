import random
from base.selenium_driver_helper import SeleniumDriverHelper
from selenium.webdriver.common.by import By
import utilities.custom_logger as cl
import logging
from pages.home.navigation_page import NavigationPage


class AddToCartPage(SeleniumDriverHelper):
    log = cl.customLogger(logging.DEBUG)

    _product_list = (By.CSS_SELECTOR, "#js-product-list .products .product")
    _add_to_cart_button = (By.CSS_SELECTOR, ".add .add-to-cart")
    _continue_shopping_button = (By.CSS_SELECTOR, ".cart-content-btn .btn-secondary")
    _proceed_to_checkout_button = (By.CSS_SELECTOR, ".cart-content-btn .btn-primary")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)


    def get_product_list(self):
        # zmiana
        products_list = self.get_elementList(*self._product_list)
        return products_list

    def select_random_product(self):
        element = self.get_product_list()
        number_of_products = len(element)
        index = random.randint(0,number_of_products-1)
        self.log.info("Category: " + self.get_title() + " | Number of product: " +
                      str(number_of_products) + " | selected item: " + str(index))
        self.element_click(element=element[index])

    def click_add_to_cart(self):
        self.element_click(*AddToCartPage._add_to_cart_button)

    def click_continue_shopping(self):
        self.wait_for_element(*AddToCartPage._continue_shopping_button, timeout=3)
        self.element_click(*AddToCartPage._continue_shopping_button)

    def click_proceed_to_checkout(self):
        self.element_click(*AddToCartPage._proceed_to_checkout_button)

    def verify_summary_cart_title(self):
        result = self.verify_page_title("Cart")
        if not result:
            result = self.verify_page_title("Koszyk")
        return result

    def verify_category_title(self, title):
        result = self.verify_page_title(title)
        return result

    def verify_number_of_product_cart(self, items=""):
        result = self.nav.get_cart_number_of_items() == items
        return result

    def add_to_cart_random_product(self):
        self.select_random_product()
        self.click_add_to_cart()
        self.click_continue_shopping()







