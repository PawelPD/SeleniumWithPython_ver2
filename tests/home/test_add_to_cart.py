from time import sleep

from pages.home.add_to_cart_page import AddToCartPage
from pages.home.login_page import LoginPage
import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
import unittest
import pytest


@pytest.mark.usefixtures("one_time_set_up", "set_up")
class AddToCartTest(unittest.TestCase):
    log = cl.custom_logger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, one_time_set_up):
        self.atc = AddToCartPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.nav = NavigationPage(self.driver)

    @pytest.mark.run(order=1)
    def test_add_products_to_cart(self):
        self.log.info("*#" * 20)
        self.log.info("test_add_products_to_cart started")
        self.log.info("*#" * 20)
        # atc = self.lp.login("pawlo1508@o2.pl", "haslotestowe") # zmiana
        self.lp.login("pawlo1508@o2.pl", "haslotestowe")
        # import wdb; wdb.set_trace()
        self.nav.click_category_clothes_men()
        result1 = self.atc.verify_category_title("Men")
        assert result1
        self.atc.add_to_cart_random_product()

        self.nav.click_category_clothes_women()
        result2 = self.atc.verify_category_title("Women")
        assert result2
        self.atc.add_to_cart_random_product()

        self.nav.click_category_accesories_stationery()
        result3 = self.atc.verify_category_title("Stationery")
        assert result3
        self.atc.add_to_cart_random_product()

        self.nav.click_category_accesories_home()
        result4 = self.atc.verify_category_title("Home Accessories")
        assert result4
        self.atc.add_to_cart_random_product()

        self.nav.click_category_art()
        result5 = self.atc.verify_category_title("Art")
        assert result5
        self.atc.add_to_cart_random_product()

        self.atc.click_proceed_to_checkout()
        result6 = self.atc.verify_summary_cart_title()
        assert result6

        result7 = self.atc.verify_number_of_product_cart(items="5")
        assert result7
