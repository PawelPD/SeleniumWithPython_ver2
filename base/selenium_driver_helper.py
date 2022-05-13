from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
from datetime import datetime
import os
from utilities.util import Util
from selenium.webdriver import ActionChains, Keys


class SeleniumDriverHelper():
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.util = Util()

    def get_title(self):
        return self.driver.title

    def get_element(self, *locator):
        element = None
        try:
            element = self.driver.find_element(*locator)
            self.log.info("Element found with locator: " + locator[1] + " and  locatorType: " + locator[0])
        except NoSuchElementException as err:
            self.log.info("Element not found with locator: " + locator[1] + " and  locatorType: "
                          + locator[0] + "ErrorInfo" + err)
        return element

    def get_element_list(self, *locator):
        """
        Get list of elements
        """
        element = None
        try:
            element = self.driver.find_elements(*locator)
            self.log.info("Element list found with locator: " + locator[1] + " and locatorType: " + locator[0])
        except:
            self.log.info("Element list not found with locator: " + locator[1] + " and locatorType: " + locator[0])
        return element

    def element_click(self, *locator, element=None):
        """
        Click on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(*locator)
            element.click()
            if locator:
                self.log.info("Clicked on element with locator: " + locator[1] + " locatorType: " + locator[0])
            else:
                self.log.info("Clicked on element: " + str(element))
        except StaleElementReferenceException as err:
            self.log.info("Cannot click on the element with locator: " + locator[1] + " locatorType: "
                          + locator[0] + "ErrorInfo" + err)

    def send_keys(self, data, *locator, element=None):
        """
        Send keys to an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(*locator)
            element.send_keys(data)
            if locator:
                self.log.info("Sent data on element with locator: " + locator[1] + " locatorType: " + locator[0])
            else:
                self.log.info("Sent data on element: " + str(element))
        except:
            self.log.info("Cannot send data on the element with locator: " + locator[1] + " locatorType: " + locator[0])

    def clear_field(self, *locator):
        """
        Clear an element field
        """
        element = self.get_element(*locator)
        element.clear()
        self.log.info("Clear field with locator: " + locator[1] + " locatorType: " + locator[0])

    def get_text(self, *locator, element=None, info=""):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator: # This means if locator is not empty
                element = self.get_element(*locator)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            text = None
        return text

    def is_element_present(self, *locator, element=None):
        """
        Check if element is present
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(*locator)

            if element is not None:
                if locator:
                    self.log.info("Element present with locator: " + locator[1] + " locatorType: " + locator[0])
                else:
                    self.log.info("Element present: " + str(element))
                return True
            else:
                self.log.info("Element not present with locator: " + locator[1] + " locatorType: " + locator[0])
                return False
        except:
            print("Element not found")
            return False

    def is_element_displayed(self, *locator):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator[0]:  # This means if locator is not empty
                element = self.get_element(*locator)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed" )
            else:
                self.log.info("Element not displayed")
            return isDisplayed
        except:
            print("Element not found")
            return False

    def element_presence_check(self, *locator):
        """
        Check if element is present
        """
        try:
            element_list = self.driver.find_elements(*locator)
            if len(element_list) > 0:
                self.log.info("Element present with locator: " + locator[1] + " locatorType: " + str(locator[0]))
                return True
            else:
                self.log.info("Element not present with locator: " + locator[1] + " locatorType: " + str(locator[0]))
                return False
        except:
            self.log.info("Element not found")
            return False
    #zmiana

    def wait_for_element(self, *locator, element=None, timeout=5, poll_frequency=0.5):
        element = None
        try:
            if locator:
                self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
                wait = WebDriverWait(self.driver, timeout=timeout,
                                     poll_frequency=poll_frequency,
                                     ignored_exceptions=[NoSuchElementException,
                                                         ElementNotVisibleException,
                                                         ElementNotSelectableException])
                element = wait.until(EC.element_to_be_clickable((locator[0], locator[1])))
            if element is not None:
                self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
                wait = WebDriverWait(self.driver, timeout=timeout,
                                     poll_frequency=poll_frequency,
                                     ignored_exceptions=[NoSuchElementException,
                                                         ElementNotVisibleException,
                                                         ElementNotSelectableException])
                element = wait.until(EC.element_to_be_clickable((element)))

            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
        return element

    def verify_page_title(self, title_to_verify):
        """
        Verify the page Title

        Parameters:
            title_to_verify: Title on the page that needs to be verified
        """
        try:
            actual_title = self.get_title()
            return self.util.verify_text_contains(actual_title, title_to_verify, match_case=True)
        except:
            self.log.error("Failed to get page title")
            return False

    def web_scroll(self, direction="up"):
        """
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def screen_shot(self, result_message):
        """
        Takes screenshot of the current open web page
        """
        dt_string = datetime.now()
        dt_string = dt_string.strftime("%d-%m-%Y_%H-%M-%S-%f")[:-3]
        file_name = result_message + "_" + str(dt_string) + ".png"
        screenshot_directory = "../screenshots/"
        relative_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot save to directory: " + destination_file)
        except:
            self.log.error("### Exception Occurred when taking screenshot")

