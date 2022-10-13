import allure

from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class SearchElement(BasePage):
    XPATH_SEARCH_INPUT = (By.XPATH, "//input[@name='search']")
    XPATH_SEARCH_BTN = (By.XPATH, "//span[@class='input-group-btn']/button")
    @allure.step(f"Клик на строку поиска.")
    def search_product(self, value):
        self._input(self.element(self.XPATH_SEARCH_INPUT), value)
        self.element(self.XPATH_SEARCH_BTN).click()
