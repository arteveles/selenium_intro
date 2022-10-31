from page_objects.HomePage import HomePage


def test_change_currency(browser):
    hp = HomePage(browser)
    hp.change_currency_on_gbp()
    hp.verify_currency_changed_on_gbp()
