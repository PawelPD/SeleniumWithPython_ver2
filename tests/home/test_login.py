from pages.home.login_page import LoginPage
import utilities.custom_logger as cl
import logging
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=1) #zbędne
    def test_invalid_login(self):
        self.log.info("*#" * 20)
        self.log.info("test_T1_invalidLogin started")
        self.log.info("*#" * 20)
        self.lp.login("wrong@email", "wrongPassword")
        result = self.lp.verify_login_failed()


    def test_sum(self):
        result = 1 + 2
        assert result == 3

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.log.info("*#" * 20)
        self.log.info("test_T2_validLogin started")
        self.log.info("*#" * 20)
        self.lp.login("pawlo1508@o2.pl", "haslotestowe")
        result1 = self.lp.verify_login_title()

        result2 = self.lp.verify_login_successful()
        print("Result1: " + str(result1))
        print("Result2: " + str(result2))

