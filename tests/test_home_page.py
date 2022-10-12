from page_objects.HomePage import HomePage
from page_objects.page_elements.SearchElement import SearchElement
from page_objects.CatalogPage import CatalogPage
from test_data.search_values import get_searched_item


def test_home_page_positive(browser):
    HomePage(browser).validate_title()


def test_home_page_menu(browser):
    HomePage(browser).validate_count_menu_items()


def test_home_page_search(browser):
    SearchElement(browser).search_product(*get_searched_item())
    CatalogPage(browser).verify_cart_product_searched(*get_searched_item())
