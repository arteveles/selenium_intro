import allure

from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class ProductCard(BasePage):
    PRODUCT_CARD = (By.XPATH, "//div[@class='product-thumb']")
    PRODUCT_CARD_NAME = (By.XPATH, "//div[@class='caption']/h4/a")
    EL1_PRODUCT_CARD = (By.XPATH, "//div[@class='product-thumb']")
    EL2_ADD_BTN = (By.XPATH, "//div[@class='button-group']/button[1]")
    EL2_ASSERTION_TEXT = "Add to Cart"
    EL3_FAVOURITE_BTN = (By.XPATH, "//div[@class='button-group']/button[2]")
    EL4_COMPARE_BTN = (By.XPATH, "//div[@class='button-group']/button[3]")
    EL5_CARD_IMAGE = (By.XPATH, "//div[@class='image']/a/img[@class='img-responsive']")

    @allure.step(f"Клик по карточке продукта. XPATH = {PRODUCT_CARD}")
    def open_product_card(self):
        product_card = self.element(self.PRODUCT_CARD)
        self.click(product_card)

    @allure.step(f"Скролл до поля видимости карточки XPATH = {PRODUCT_CARD_NAME}")
    def product_card_name(self):
        assert self.element(self.PRODUCT_CARD_NAME).location_once_scrolled_into_view

    @allure.step(f"Добавление товара в карзину.")
    def product_card_add_to_cart(self):
        add_btn = self.element(self.EL2_ADD_BTN).text.lower()
        add_btn_assertion = self.EL2_ASSERTION_TEXT.lower()
        assert add_btn == add_btn_assertion

    @allure.step(f"Добавление товара в список желаемого.")
    def product_card_add_to_wish_list(self):
        assert self.element(self.EL3_FAVOURITE_BTN)

    @allure.step(f"Добавление товара в список сравнения.")
    def product_card_compare_btn(self):
        assert self.element(self.EL4_COMPARE_BTN)

    @allure.step(f"Проверка наличия изображения в карточке товара.")
    def product_card_image(self):
        assert self.element(self.EL5_CARD_IMAGE)
