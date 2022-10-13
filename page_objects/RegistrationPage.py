import allure

from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from test_data.product_values import now


class RegistrationPage(BasePage):
    FN_INPUT = (By.XPATH, "//input[@name='firstname']")
    LN_INPUT = (By.XPATH, "//input[@name='lastname']")
    MAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PHONE_INPUT = (By.XPATH, "//input[@name='telephone']")
    PASS_INPUT = (By.XPATH, "//input[@name='password']")
    CONFIRM_INPUT = (By.XPATH, "//input[@name='confirm']")
    RADIOBTN_NO = (By.XPATH, "//input[@type='radio' and @value='0']")
    PRIVACY_CHK = (By.XPATH, "//input[@type='checkbox' and @value='1']")
    SUBMIT_BTN = (By.XPATH, "//input[@type='submit']")

    @allure.step(f"Ввод имени.")
    def input_name(self):
        name = f"test_{now}"
        self._input(self.element(self.FN_INPUT), name)

    @allure.step(f"Ввод фамилии.")
    def input_last_name(self):
        name = f"test_{now}"
        self._input(self.element(self.LN_INPUT), name)

    @allure.step(f"Ввод мэила.")
    def input_mail(self):
        name = f"test_{now}"
        domen = "@gmail.com"
        self._input(self.element(self.MAIL_INPUT), name + domen)

    @allure.step(f"Ввод номера.")
    def input_phone(self):
        phone = f"+79999999999"
        self._input(self.element(self.PHONE_INPUT), phone)

    @allure.step(f"Ввод пароля. Подтверждение пароля.")
    def input_pass_and_confirm(self):
        passw = f"test_{now}"
        self._input(self.element(self.PASS_INPUT), passw)
        self._input(self.element(self.CONFIRM_INPUT), passw)

    @allure.step(f"Не подписываемся на рассылку новостей.")
    def newsletter(self):
        self.element(self.RADIOBTN_NO).click()

    @allure.step(f"Соглашаемся с политикой конфиденциальности.")
    def privacy(self):
        self.element(self.PRIVACY_CHK).click()

    @allure.step(f"Нажиаем кнопку подтвердить.")
    def submit(self):
        self.element(self.SUBMIT_BTN).click()
