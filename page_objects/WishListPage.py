import allure

from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class WishListPage(BasePage):
    TABLE_DEL_BTN = (By.XPATH, "//table/tbody/tr/td[@class='text-right']/a")
    WL_BTN = (By.XPATH, "//a[@id='wishlist-total']")

    @allure.step(f"Валидация добавления товара в список желаний.")
    def check_items_in_list(self):
        self.element(self.WL_BTN).click()
        assert self.element(self.TABLE_DEL_BTN)
