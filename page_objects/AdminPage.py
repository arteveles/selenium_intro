import time

from test_data.alert_values import accept
from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class AdminPage(BasePage):
    NAV_MENU = (By.XPATH, "//nav[@id='column-left']")
    CATALOG_ITEM = (By.XPATH, "//li[@id='menu-catalog']")
    PRODUCT_ITEM = (By.XPATH, "//a[text()='Products']")
    ADD_BTN = (By.XPATH, "//div[@class='pull-right']/a")
    PROD_NAME_INP = (By.XPATH, "//input[@id='input-name1']")
    DESCR_PROD_TEXT_AREA = (By.XPATH, "//div[@class='note-editing-area']//div[@role='textbox']")
    META_TAG = (By.XPATH, "//input[@id='input-meta-title1']")
    MENU_BAR_DATA = (By.XPATH, "//ul[@class='nav nav-tabs']//a[text()='Data']")
    MODEL_INP = (By.XPATH, "//input[@id='input-model']")
    SAVE_BTN = (By.XPATH, "//button[@data-original-title='Save']")
    TABLE_ROW = (By.XPATH, "//tbody//td[@class='text-left']")
    TABLE_BODY = (By.XPATH, "//tbody")
    ALERT_SUCCESS = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    PAGIN_LEFT = (By.XPATH, "//ul[@class='pagination']/lI/a[text()='>']")
    CHKBOX = (By.XPATH, "//input[@type='checkbox']")
    DEL_BTN = (By.XPATH, "//button[@class='btn btn-danger']")

    # //tbody/tr/td[@class='text-left']

    def select_catalog_product_item(self):
        self.element_in_element(self.NAV_MENU, self.CATALOG_ITEM).click()
        self.element(self.PRODUCT_ITEM).click()

    def add_new_product(self, product_name):
        self.element(self.ADD_BTN).click()
        self._input(self.element(self.PROD_NAME_INP), product_name)
        self._input(self.element(self.DESCR_PROD_TEXT_AREA), product_name)
        self._input(self.element(self.META_TAG), product_name)
        self.element(self.MENU_BAR_DATA).click()
        self._input(self.element(self.MODEL_INP), product_name)
        self.element(self.SAVE_BTN).click()

    def alert_success_add(self):
        self.element(self.ALERT_SUCCESS)

    def verify_product_add(self, product_name):
        while product_name != self.element(self.TABLE_ROW).text:
            self.element(self.PAGIN_LEFT).click()

    def remove_product(self, product_name):
        while product_name != self.element(self.TABLE_ROW).text:
            self.element(self.PAGIN_LEFT).click()
        if self.element(self.TABLE_ROW).text == product_name:
            self.element_in_element(self.TABLE_BODY, self.CHKBOX).click()
            self.element(self.DEL_BTN).click()
        else:
            ValueError("Тестовый продукт не создан")

    def alert_accept(self):
        self.switch_to_alert_frame(accept())
