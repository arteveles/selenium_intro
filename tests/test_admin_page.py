from selenium.webdriver.common.by import By
import time
from data_storage import EL_5_VERIFY_ASSERT_TEXT
from data_storage import EL_4_ALERT_ASSERT_TEXT_2
from data_storage import AP_URL
from data_storage import EL_1_INP_UN_NEGAV
from data_storage import EL_1_INP_UN_POSITV
from data_storage import EL_1_INP_USERN
from data_storage import EL_2_INP_PASS_POSIV
from data_storage import EL_2_INP_PASS_NEGAV
from data_storage import EL_2_INP_PASS
from data_storage import EL_4_ALERT_ASSERT_TEXT
from data_storage import EL_5_VERIFY
from data_storage import EL_4_ALERT
from data_storage import EL_3_LOG_BTN


def test_valid_reg(driver):
    driver.get(url=AP_URL)
    input_un = driver.find_element(By.XPATH, EL_1_INP_USERN)
    input_un.click()
    input_un.clear()
    input_un.send_keys(EL_1_INP_UN_POSITV)
    time.sleep(1)
    input_pv = driver.find_element(By.XPATH, EL_2_INP_PASS)
    input_pv.click()
    input_pv.clear()
    input_pv.send_keys(EL_2_INP_PASS_POSIV)
    time.sleep(1)
    submit_btn = driver.find_element(By.XPATH, EL_3_LOG_BTN)
    submit_btn.click()
    time.sleep(2)
    verify_logout = driver.find_element(By.XPATH, EL_5_VERIFY)
    assert verify_logout.text == EL_5_VERIFY_ASSERT_TEXT


def test_invalid_reg(driver):
    driver.get(url=AP_URL)
    input_un = driver.find_element(By.XPATH, EL_1_INP_USERN)
    input_un.click()
    input_un.clear()
    input_un.send_keys(EL_1_INP_UN_NEGAV)
    time.sleep(1)
    input_pv = driver.find_element(By.XPATH, EL_2_INP_PASS)
    input_pv.click()
    input_pv.clear()
    input_pv.send_keys(EL_2_INP_PASS_NEGAV)
    time.sleep(1)
    submit_btn = driver.find_element(By.XPATH, EL_3_LOG_BTN)
    submit_btn.click()
    time.sleep(2)
    alert = driver.find_element(By.XPATH, EL_4_ALERT)
    assert alert.text == EL_4_ALERT_ASSERT_TEXT or EL_4_ALERT_ASSERT_TEXT_2
    print(alert.text)
    print(EL_4_ALERT_ASSERT_TEXT)
