import pytest
import os
from selenium import webdriver
from data_storage import URL_OPENCART
from selenium.webdriver import ChromeOptions, FirefoxOptions


def pytest_addoption(parser):
    """
    Выбор браузера. По умолчанию, если не передан аргумент в командную строку - запустится FireFox
    """
    parser.addoption(
        "--browser", default="firefox", help="firefox browser"
    )
    parser.addoption(
        "--drivers", default=os.path.expanduser("~/dev/driver/")
    )
    """
    Отработка тестов без открытия окна браузера
    """
    parser.addoption(
        "--headless", action="store_true"
    )
    parser.addoption(
        "--base_url", default=URL_OPENCART
    )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--base_url")

    if browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.headless = True
        _driver = webdriver.Firefox(executable_path=os.path.expanduser(f"{drivers}/geckodriver"), options=options)
    elif browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.headless = True
        _driver = webdriver.Chrome(executable_path=os.path.expanduser(f"{drivers}/chromedriver"), options=options)
    elif browser_name == "opera":
        _driver = webdriver.Opera(executable_path=os.path.expanduser(f"{drivers}/operadriver"))
    else:
        raise ValueError(f"Browser {browser_name} is not supported")

    _driver.maximize_window()
    _driver.base_url = base_url

    yield _driver

    _driver.close()
