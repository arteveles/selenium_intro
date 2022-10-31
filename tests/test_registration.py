import time
from selenium.webdriver.common.by import By
from data_storage import REG_PAGE, EL_REG_ASSERT
from data_storage import EL_REG_FN, EL_REG_LN
from data_storage import EL_REG_FN_VALUE, EL_REG_LN_VALUE
from data_storage import EL_REG_MAIL, EL_REG_PHONE
from data_storage import EL_REG_MAIL_VALUE, EL_REG_PHONE_VALUE
from data_storage import EL_REG_PASS, EL_REG_PASS_CONFIRM
from data_storage import EL_REG_PASS_VALUE, EL_REG_PASS_CONFIRM_VALUE
from data_storage import EL_REG_NO_RDB, EL_REG_CHBX, EL_REG_CONT_BTN

"""Регистрация пользователя"""


def test_registration(driver):
    driver.get(url=REG_PAGE)
    first_name = driver.find_element(By.XPATH, EL_REG_FN)
    first_name.click()
    first_name.clear()
    first_name.send_keys(EL_REG_FN_VALUE)
    time.sleep(1)
    last_name = driver.find_element(By.XPATH, EL_REG_LN)
    last_name.click()
    last_name.clear()
    last_name.send_keys(EL_REG_LN_VALUE)
    time.sleep(1)
    mail = driver.find_element(By.XPATH, EL_REG_MAIL)
    mail.click()
    mail.clear()
    mail.send_keys(EL_REG_MAIL_VALUE)
    time.sleep(1)
    phone = driver.find_element(By.XPATH, EL_REG_PHONE)
    phone.click()
    phone.clear()
    phone.send_keys(EL_REG_PHONE_VALUE)
    time.sleep(1)
    passw = driver.find_element(By.XPATH, EL_REG_PASS)
    passw.click()
    passw.clear()
    passw.send_keys(EL_REG_PASS_VALUE)
    time.sleep(1)
    passw_confirm = driver.find_element(By.XPATH, EL_REG_PASS_CONFIRM)
    passw_confirm.click()
    passw_confirm.clear()
    passw_confirm.send_keys(EL_REG_PASS_CONFIRM_VALUE)
    time.sleep(1)
    radio_btn_no = driver.find_element(By.XPATH, EL_REG_NO_RDB)
    radio_btn_no.click()
    time.sleep(1)
    chbk_agree = driver.find_element(By.XPATH, EL_REG_CHBX)
    chbk_agree.click()
    btn_continue = driver.find_element(By.XPATH, EL_REG_CONT_BTN)
    btn_continue.click()
    time.sleep(2)
    assert EL_REG_ASSERT
