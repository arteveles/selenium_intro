import datetime
import json
import logging

from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
import allure
import pytest
import os
from selenium import webdriver

DRIVERS = os.path.expanduser("~/dev/driver")


# """Конфигурируем логгер глобально и наблюдаем сайдэффект"""
# logging.basicConfig(level=logging.INFO, filename="logs/test.log")
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


    """Создается новый логгер, и берется имя теста который сейчас выполняеся.
    Чтоб на отдельный тест создавался отдельный лог."""
    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(filename=f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))


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

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities, indent=4),
        attachment_type=allure.attachment_type.JSON
    )

    driver.logger = logger
    driver.test_name = request.node.name
    driver.log_level = log_level

    logger.info("Browser:{}".format(browser, driver.desired_capabilities))

    def fin():
        driver.quit()
        logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)

    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(5)
    return driver
