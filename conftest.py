import datetime
import json
import logging
from browsermobproxy import Server, Client
from selenium.webdriver import DesiredCapabilities
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
def proxy_server(request):
    server = Server("browsermob-proxy/bin/browsermob-proxy")
    server.start()
    client = Client("http://10.0.2.15:8081/")

    server.create_proxy()
    request.addfinalizer(server.stop)
    client.new_har()
    return client


@pytest.fixture
def browser(request, proxy_server):
    url = request.config.getoption("--url")
    browser_select = request.config.getoption("--browser_select")
    executor = request.config.getoption("--executor")
    log_level = request.config.getoption("--log_level")

    """Установка прокси сервера"""
    caps = {}
    proxy_server.add_to_webdriver_capabilities(caps)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        executable_path=f"{DRIVERS}/chromedriver",
        options=options,
        desired_capabilities=caps
    )

    """Создается новый логгер, и берется имя теста который сейчас выполняеся.
    Чтоб на отдельный тест создавался отдельный лог."""
    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(filename=f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

    # https://www.selenium.dev/documentation/en/webdriver/page_loading_strategy/
    # common_caps = {"pageLoadStrategy": "none"}
    caps = DesiredCapabilities.CHROME
    options = webdriver.ChromeOptions()
    options.accept_insecure_certs = True

    """Определяем уровень логирования как самый подробный. Для браузера и производительности."""
    caps['goog:LoggingPrefs'] = {
        'browser': 'ALL',
        'performance': 'ALL',
    }

    if browser_select == "firefox":
        driver = webdriver.Firefox(
            executable_path=f"{DRIVERS}/geckodriver",
            desired_capabilities=caps
        )

    elif browser_select == "chrome":
        driver = webdriver.Chrome(
            executable_path=f"{DRIVERS}/chromedriver",
            desired_capabilities=caps
        )

    elif browser_select == "opera":
        driver = webdriver.Opera(
            executable_path=f"{DRIVERS}/operadriver",
            desired_capabilities=caps
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

    driver.proxy = proxy_server
    driver.logger = logger
    driver.test_name = request.node.name
    driver.log_level = log_level

    logger.info("Browser:{}".format(browser, driver.desired_capabilities))

    def fin():
        # dump_log_to_json(driver.proxy.har['log'], f"{request.node.name}.json") # раскомментировать, если потребуется спроксировать трафик
        # driver.proxy.close()
        driver.quit()
        logger.info("===> Test {} passed at {}".format(request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)

    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(5)
    return driver


def dump_log_to_json(har_log, file_name):
    logs = []
    with open(file_name, "w+") as f:
        for i, el in enumerate(har_log["entries"], start=1):
            logs.append({i: {"request": el["request"], "response": el["response"]}})
        f.write(json.dumps(logs))
