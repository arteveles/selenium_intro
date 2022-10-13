import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step(f"Клик на элемент.")
    def click(self, element):
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    @allure.step(f"Ввод данных.")
    def _input(self, element, value):
        self.click(element)
        element.clear()
        element.send_keys(value)

    @allure.step(f"Поиск элемента в элементе.")
    def element_in_element(self, parent_locator: tuple, child_locator: tuple):
        return self.element(parent_locator).find_element(*child_locator)

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

    @allure.step(f"Проверка наименования продукта.")
    def verify_product_item(self, product_name):
        return self.element((By.LINK_TEXT, product_name))

    @allure.step(f"Переключение на алерт, с целью принять или отклонить.")
    def switch_to_alert_frame(self, accept_or_decline):
        WebDriverWait(self.driver, 5).until(EC.alert_is_present(), "Не появился алерт")
        return eval(f"self.driver.switch_to.alert.{accept_or_decline}")
