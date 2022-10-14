import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage



class AdminLoginPage(BasePage):
    INPUT_USERN = (By.XPATH, "//input[@name='username']")
    INPUT_PASS = (By.XPATH, "//input[@name='password']")
    LOG_BTN = (By.XPATH, "//button[@type='submit']")
    LOGOUT_BTN = (By.XPATH, "//span[@class='hidden-xs hidden-sm hidden-md']")
    ALERT_TEXT = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")

    @allure.step(f"Авторизация в админке.")
    def authorization(self, username, password):
        with allure.step("Ввод логина и пароля:"):
            try:
                self._input(self.element(self.INPUT_USERN), username)
                self._input(self.element(self.INPUT_PASS), password)
                self.click(self.element(self.LOG_BTN))
                return self
            except NoSuchElementException as e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    @allure.step(f"Не авторизован? Alert XPATH = {ALERT_TEXT}")
    def validate_no_authorization(self):
        self.element(self.ALERT_TEXT)

    @allure.step(f"Клик на кнопку разлогиниться. XPATH = {LOGOUT_BTN}")
    def logout(self):
        logout_btn = self.element(self.LOGOUT_BTN)
        logout_btn.click()
