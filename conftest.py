import json

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


@pytest.fixture
def browser(request):
    url = request.config.getoption("--url")
    browser_select = request.config.getoption("--browser_select")

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
        body=json.dumps(driver.capabilities),
        attachment_type=allure.attachment_type.JSON
    )

    request.addfinalizer(driver.quit)

    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(5)
    return driver
