import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AddProdMenuElem(BasePage):
    MENU_BAR = (By.XPATH, "//input[@id='input-meta-title1']")
    @allure.step(f"Выбор пункта в меню")
    def choose_data(self):
        self.element(self.MENU_BAR)[1].click
