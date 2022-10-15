import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException as e



class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        with allure.step(f"Клик на элемент."):
            try:
                ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def _input(self, element, value):
        with allure.step(f"Ввод данных."):
            try:
                self.click(element)
                element.clear()
                element.send_keys(value)
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def element_in_element(self, parent_locator: tuple, child_locator: tuple):
        with allure.step(f"Поиск элемента в элементе."):
            try:
                return self.element(parent_locator).find_element(*child_locator)
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    @allure.step(f"Поиск и ожидание элемента.")
    def element(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента {locator}")

    @allure.step(f"Поиск и ожидание элементов.")
    def elements(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элементов {locator}")

    def verify_product_item(self, product_name):
        with allure.step(f"Проверка наименования продукта."):
            try:
                return self.element((By.LINK_TEXT, product_name))
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)


    def switch_to_alert_frame(self, accept_or_decline):
        with allure.step(f"Переключение на алерт, с целью принять или отклонить."):
            try:
                WebDriverWait(self.driver, 5).until(EC.alert_is_present(), "Не появился алерт")
                return eval(f"self.driver.switch_to.alert.{accept_or_decline}")
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)
