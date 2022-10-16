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

    class MyLogger(AbstractEventListener):
        """Создается новый логгер, и берется имя теста который сейчас выполняеся.
        Чтоб на отдельный тест создавался отдельный лог."""
        logger = logging.getLogger(request.node.name)
        logger.setLevel(logging.INFO)
        ch = logging.FileHandler(filename=f"logs/{request.node.name}.log")
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(logging.Formatter('%(asctime)s:%(name)s:%(levelname)s: %(message)s'))

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

        def after_quit(self, driver):
            self.logger.info(f"Driver Quit")

        # def on_exception(self, exception, driver):
        #     self.logger.error(f'Oops i got {exception}')
        #     driver.save_screenshot(f'logs/{driver.session_id}.png')

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

    else:
        driver = webdriver.Remote(
            command_executor="http://{}:4444/wd/hub".format(executor),
            desired_capabilities={"browserName": browser}
        )

    driver = EventFiringWebDriver(driver, MyLogger())
    driver.test_name = request.node.name
    driver.log_level = log_level

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities, indent=4),
        attachment_type=allure.attachment_type.JSON
    )

    def fin():
        driver.quit()

    request.addfinalizer(fin)

    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(5)
    return driver
