from selenium.webdriver.common.by import By

from data_storage import URL_PRODUCT_CARD
from data_storage import EL3_FAVOURITE_BTN
from data_storage import EL2_ADD_BTN
from data_storage import EL1_PRODUCT_CARD
from data_storage import EL5_CARD_IMAGE
from data_storage import EL2_ASSERTION_TEXT
from data_storage import EL4_COMPARE_BTN


def test_product_card_fixture(driver):
    driver.get(url=URL_PRODUCT_CARD)
    product_card = driver.find_element(By.XPATH, EL1_PRODUCT_CARD)
    assert product_card
    add_btn = driver.find_element(By.XPATH, EL2_ADD_BTN)
    assert add_btn.text.lower() == EL2_ASSERTION_TEXT.lower()
    favourite_btn = driver.find_element(By.XPATH, EL3_FAVOURITE_BTN)
    assert favourite_btn
    compare_btn = driver.find_element(By.XPATH, EL4_COMPARE_BTN)
    assert compare_btn
    card_image = driver.find_element(By.XPATH, EL5_CARD_IMAGE)
    assert card_image
