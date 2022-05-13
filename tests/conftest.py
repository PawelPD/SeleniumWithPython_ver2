import pytest
from base.webdriver_factory import WebDriverFactory


@pytest.fixture()
def set_up():
    print("Running method level set_up")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def one_time_set_up(request, browser):
    print("Running one time set_up")
    wdf = WebDriverFactory(browser)
    driver = wdf.get_web_driver_instance()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--os_type", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--os_type")
