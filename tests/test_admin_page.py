from page_objects.AdminLoginPage import AdminLoginPage
from page_objects.AdminPage import AdminPage
from test_data.users import get_valid_user, get_invalid_user
from test_data.product_values import product_name


def test_valid_registration(browser):
    alp = AdminLoginPage(browser)
    alp.authorization(*get_valid_user())
    alp.logout()


def test_invalid_registration(browser):
    alp = AdminLoginPage(browser)
    alp.authorization(*get_invalid_user())
    alp.validate_no_authorization()


def test_add_new_product(browser):
    ap = AdminPage(browser)
    alp = AdminLoginPage(browser)
    alp.authorization(*get_valid_user())
    ap.select_catalog_product_item()
    ap.add_new_product(*product_name())
    ap.alert_success_add()
    ap.verify_product_add(*product_name())


def test_remove_new_product(browser):
    ap = AdminPage(browser)
    alp = AdminLoginPage(browser)
    alp.authorization(*get_valid_user())
    ap.select_catalog_product_item()
    ap.remove_product(*product_name())
    ap.alert_accept()
