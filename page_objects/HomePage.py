import allure
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

    @allure.step(f"Клик на кнопку регистрации. XPATH = {REG_BTN}")
    def click_registrate(self):
        self.element(self.MYAKK_SELECT).click(),
        self.element(self.REG_BTN).click()

    @allure.step(f"Смена отображения цены товара в валюте. 1_XPATH = {CURRENCY}, 2_XPATH = {CURRENCY_GBP}")
    def change_currency_on_gbp(self):
        self.element(self.CURRENCY).click()
        self.element(self.CURRENCY_GBP).click()

    @allure.step(f"Проверка смены цены товара на валюту.")
    def verify_currency_changed_on_gbp(self):
        assert self.element(self.VERIFY_GBP)
        assert self.element(self.VERIFY_GBP_2)

    @allure.step(f"Выбор списка компов из менюшки")
    def select_all_desktops(self):
        self.element(self.MENU_DESKTOP).click()
        self.element(self.CATALOG_SEE_ALL).click()

    @allure.step(f"Сверка количества мониторов: значения одинаковы в менюшке и на странице каталога товара.")
    def check_count_of_monitors(self):
        self.element(self.MENU_COMPONENTS).click()
        num = re.findall(r"\d+", self.element(self.CTG_COMPARE_ITEMS).text)
        self.element(self.CTG_COMPARE_ITEMS).click()
        count_prod = self.elements(self.COUNT_PRODUCTS)
        assert str(len(count_prod)) == num[0]

    @allure.step(f"Валидация наименования.")
    def validate_title(self):
        title = self.driver.title
        assert title == self.TITLE

    @allure.step(f"Валидация количества пунктов меню.")
    def validate_count_menu_items(self):
        count_menu_items = len(self.elements(self.MENU_LIST))
        assert count_menu_items == 8
