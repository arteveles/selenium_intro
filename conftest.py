import json
import logging

from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
import allure
import pytest
import os
from selenium import webdriver

DRIVERS = os.path.expanduser("~/dev/driver")


def pytest_addoption(parser):
    """Аргумент базовой ссылки сайта"""
    parser.addoption(
        "--url", "-U", default="http://10.0.2.15:8081/"
    )

    """Аргумент выбора браузера"""
    parser.addoption(
        "--browser_select", "-B", default="firefox"
    )

    parser.addoption(
        "--executor", action="store", default="127.0.0.1"
    )

    parser.addoption(
        "--log_level", action="store", default="DEBUG"
    )


@pytest.fixture
def browser(request):
    url = request.config.getoption("--url")
    browser_select = request.config.getoption("--browser_select")
    executor = request.config.getoption("--executor")
    log_level = request.config.getoption("--log_level")

    class MyListener(AbstractEventListener):
        logger = logging.getLogger(request.node.name)
        logger.setLevel(logging.INFO)
        ch = logging.FileHandler(filename=f"logs/{request.node.name}.log")
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(logging.Formatter('%(name)s:%(levelname)s: %(message)s'))

        def before_navigate_to(self, url, driver):
            self.logger.info(f"I`m navigate to {url} and {driver.title}")

        def after_navigate_to(self, url, driver):
            self.logger.info(f"I`m on {url}")

        def before_navigate_back(self, driver):
            self.logger.info(f"I`m navigating back")

        def after_navigate_back(self, driver):
            self.logger.info(f"I`m back")

        def before_find(self, by, value, driver):
            self.logger.info(f"I`m looking for '{value}' with '{by}'")

        def before_click(self, element, driver):
            self.logger.info(f"I`m clicking {element}")

        def after_click(self, element, driver):
            self.logger.info(f"I`ve clicked {element}")

        def before_execute_script(self, script, driver):
            self.logger.info(f"I`m executing {script}")

        def after_execute_script(self, script, driver):
            self.logger.info(f"I`ve executed {script}")

        def before_quit(self, driver):
            self.logger.info(f"I`m getting ready to terminate {driver}")

        # def after_quit(self, driver):

    # https://www.selenium.dev/documentation/en/webdriver/page_loading_strategy/
    common_caps = {"pageLoadStrategy": "none"}

    if browser_select == "firefox":
        driver = webdriver.Firefox(
            executable_path=f"{DRIVERS}/geckodriver",
            desired_capabilities=common_caps
        )

    elif browser_select == "chrome":
        driver = webdriver.Chrome(
            executable_path=f"{DRIVERS}/chromedriver",
            desired_capabilities=common_caps
        )

    elif browser_select == "opera":
        driver = webdriver.Opera(
            executable_path=f"{DRIVERS}/operadriver",
            desired_capabilities=common_caps
        )

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities, indent=4),
        attachment_type=allure.attachment_type.JSON
    )

    request.addfinalizer(driver.quit)

    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(5)
    return driver
