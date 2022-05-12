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
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.util = Util()

    def get_title(self):
        return self.driver.title

    def get_element(self, locatorType, locator):
        element = None
        try:
            element = self.driver.find_element(locatorType, locator)
            self.log.info("Element found with locator: " + locator + " and  locatorType: " + locatorType)
        except NoSuchElementException as err:
            self.log.info("Element not found with locator: " + locator + " and  locatorType: " + locatorType + "tekst do dodania" + err)
        return element

    def get_elementList(self, locatorType="", locator=""):
        """
        Get list of elements
        """
        element = None
        try:
            element = self.driver.find_elements(locatorType, locator)
            self.log.info("Element list found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator: " + locator + " and locatorType: " + locatorType)
        return element

    def element_click(self, locatorType="", locator="", element=None):
        """
        Click on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locatorType, locator)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except E:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def send_keys(self, data, locatorType="", locator="", element=None):
        """
        Send keys to an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locatorType, locator)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def clear_field(self, locatorType="", locator=""):
        """
        Clear an element field
        """
        element = self.get_element(locatorType, locator)
        element.clear()
        self.log.info("Clear field with locator: " + locator + " locatorType: " + locatorType)

    def get_text(self, locatorType="", locator="", element=None, info=""):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator: # This means if locator is not empty
                element = self.get_element(locatorType, locator)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def is_element_present(self, locatorType="", locator="", element=None):
        """
        Check if element is present
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locatorType, locator)

            if element is not None:
                self.log.info("Element present with locator: " + locator + " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator + " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False

    def is_element_displayed(self, *locatorType):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locatorType:  # This means if locator is not empty
                element = self.get_element(locatorType, locator)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed" )
            else:
                self.log.info("Element not displayed")
            return isDisplayed
        except:
            print("Element not found")
            return False

    def element_presence_check(self, locatorType="", locator=""):
        """
        Check if element is present
        """
        try:
            elementList = self.driver.find_elements(locatorType, locator)
            if len(elementList) > 0:
                self.log.info("Element present with locator: " + locator + " locatorType: " + str(locatorType))
                return True
            else:
                self.log.info("Element not present with locator: " + locator + " locatorType: " + str(locatorType))
                return False
        except:
            self.log.info("Element not found")
            return False
    #zmiana
    def wait_for_element(self, locatorType="", locator="",
                         timeout=5, pollFrequency=0.5, expectedCond):
        element = None
        try:
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((locatorType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def verify_page_title(self, titleToVerify):
        """
        Verify the page Title

        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.get_title()
            return self.util.verify_text_contains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
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

    def screen_shot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        dt_string = datetime.now()
        dt_string = dt_string.strftime("%d-%m-%Y_%H-%M-%S-%f")[:-3]
        fileName = resultMessage + "_" + str(dt_string) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()