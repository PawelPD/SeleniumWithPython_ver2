"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.get_web_driver_instance()
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class WebDriverFactory:

    def __init__(self, browser):
        self.browser = browser

    def get_web_driver_instance(self):
        baseURL = "http://sklepdemo.polomski.ayz.pl/ecommerce/index.php"
        # baseURL = "https://courses.letskodeit.com/"
        if self.browser == "chrome":
            service = Service("..\\..\\configfiles\\chromedriver.exe")
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(service=service, options=options)
        elif self.browser == "firefox":
            service = Service("..\\..\\configfiles\\geckodriver.exe")
            driver = webdriver.Firefox(service=service)
        elif self.browser == "iexplorer":
            service = Service("..\\..\\configfiles\\IEDriverServer.exe")
            driver = webdriver.Ie(service=service)
        else:
            service = Service("..\\..\\configfiles\\geckodriver.exe")
            driver = webdriver.Firefox(service=service)
        driver.implicitly_wait(1)
        driver.maximize_window()
        driver.get(baseURL)
        return driver
