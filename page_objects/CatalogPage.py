from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    CATALOG_HEADER = (By.XPATH, "//div[@class='col-sm-9']/h2")
    CATALOG_BTN_ADD_TO_FVT = (By.XPATH, "//div[@class='button-group']/button[2]")
    LOGIN_LINK = (By.XPATH, "//a[text()='login']")
    LOGIN_BTN = (By.XPATH, "//input[@value='Login']")
    EMAIL_INP = (By.XPATH, "//input[@name='email']")
    PASSW_INP = (By.XPATH, "//input[@name='password']")
    PROD_NAME = (By.XPATH, "//div[@class='product-thumb']//h4/a")
    CATALOG_HEADER_TEXT = "Desktops"


def verify_header_of_page(self):
    desktop_header = self.element(self.CATALOG_HEADER)
    assert desktop_header.text == self.CATALOG_HEADER_TEXT


def add_to_wish_list(self):
    self.element(self.CATALOG_BTN_ADD_TO_FVT).click()


def login_from_alert(self, email, password):
    self.element(self.LOGIN_LINK).click()
    self._input(self.element(self.EMAIL_INP), email)
    self._input(self.element(self.PASSW_INP), password)
    self.element(self.LOGIN_BTN).click()
    return self


def verify_cart_product_searched(self, product_name_value):
    product_name = self.element(self.PROD_NAME).text
    assert product_name == product_name_value
