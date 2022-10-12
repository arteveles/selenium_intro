from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AdminLoginPage(BasePage):
    INPUT_USERN = (By.XPATH, "//input[@name='username']")
    INPUT_PASS = (By.XPATH, "//input[@name='password']")
    LOG_BTN = (By.XPATH, "//button[@type='submit']")
    LOGOUT_BTN = (By.XPATH, "//span[@class='hidden-xs hidden-sm hidden-md']")
    ALERT_TEXT = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")

    def authorization(self, username, password):
        self._input(self.element(self.INPUT_USERN), username)
        self._input(self.element(self.INPUT_PASS), password)
        self.click(self.element(self.LOG_BTN))
        return self

    def validate_no_authorization(self):
        self.element(self.ALERT_TEXT)

    def logout(self):
        logout_btn = self.element(self.LOGOUT_BTN)
        logout_btn.click()
