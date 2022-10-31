from page_objects.HomePage import HomePage
from page_objects.RegistrationPage import RegistrationPage


def test_registration(browser):
    hp = HomePage(browser)
    rp = RegistrationPage(browser)
    hp.click_registrate()
    rp.input_name()
    rp.input_last_name()
    rp.input_mail()
    rp.input_phone()
    rp.input_pass_and_confirm()
    rp.newsletter()
    rp.privacy()
    rp.submit()
