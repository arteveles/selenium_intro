import allure

from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from test_data.search_values import _searched_item


class ProductPage(BasePage):
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-4']/h1")

    @allure.step(f"Валидация имени продукта. XPATH = {PRODUCT_NAME}")
    def verify_product_name(self):
        product_name = self.element(self.PRODUCT_NAME).text
        assert product_name == _searched_item[0]
