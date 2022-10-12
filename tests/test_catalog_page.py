from page_objects.CatalogPage import CatalogPage
from page_objects.HomePage import HomePage
from page_objects.WishListPage import WishListPage
from test_data.users import login_user


def test_visit_catalog_from_menu(browser):
    hp = HomePage(browser)
    cp = CatalogPage(browser)
    hp.select_all_desktops()
    cp.verify_header_of_page()


def test_catalog_add_to_favourite(browser):
    hp = HomePage(browser)
    cp = CatalogPage(browser)
    wlp = WishListPage(browser)
    hp.select_all_desktops()
    cp.add_to_wish_list()
    cp.login_from_alert(*login_user())
    wlp.check_items_in_list()


def test_compare_count_prod(browser):
    hp = HomePage(browser)
    hp.check_count_of_monitors()
