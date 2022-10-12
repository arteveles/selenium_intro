from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from page_objects.page_elements.SearchElement import SearchElement
from test_data.search_values import get_searched_item

import re


class HomePage(BasePage):
    MYAKK_SELECT = (By.XPATH, "//span[text()='My Account']")
    REG_BTN = (By.XPATH, "//li/a[text()='Register']")
    CURRENCY = (By.XPATH, "//span[text()='Currency']")
    CURRENCY_GBP = (By.XPATH, "//button[@name='GBP']")
    VERIFY_GBP = (By.XPATH, "//strong[text()='£']")
    VERIFY_GBP_2 = (By.XPATH, "//div[@class='row']//p[contains(text(), '£')]")
    CATALOG_SEE_ALL = (By.XPATH, "//div[@class='dropdown-menu']/a[text() = 'Show All Desktops']")
    MENU_DESKTOP = (By.XPATH, "//ul[@class='nav navbar-nav']/li/a[text()='Desktops']")
    MENU_COMPONENTS = (By.XPATH, "//a[text()='Components']")
    CTG_COMPARE_ITEMS = (By.XPATH, "//ul[@class='nav navbar-nav']/child::li[3]//child::li[2]/a")
    COUNT_PRODUCTS = (By.XPATH, "//div[@id='content']/div[3]/div")
    TITLE = "Your Store"
    MENU_LIST = (By.XPATH, "//ul[@class='nav navbar-nav']/li")

    def click_registrate(self):
        self.element(self.MYAKK_SELECT).click(),
        self.element(self.REG_BTN).click()

    def change_currency_on_gbp(self):
        self.element(self.CURRENCY).click()
        self.element(self.CURRENCY_GBP).click()

    def verify_currency_changed_on_gbp(self):
        assert self.element(self.VERIFY_GBP)
        assert self.element(self.VERIFY_GBP_2)

    def select_all_desktops(self):
        self.element(self.MENU_DESKTOP).click()
        self.element(self.CATALOG_SEE_ALL).click()

    def check_count_of_monitors(self):
        self.element(self.MENU_COMPONENTS).click()
        num = re.findall(r"\d+", self.element(self.CTG_COMPARE_ITEMS).text)
        self.element(self.CTG_COMPARE_ITEMS).click()
        count_prod = self.elements(self.COUNT_PRODUCTS)
        assert str(len(count_prod)) == num[0]

    def validate_title(self):
        title = self.driver.title
        assert title == self.TITLE

    def validate_count_menu_items(self):
        count_menu_items = len(self.elements(self.MENU_LIST))
        assert count_menu_items == 8
