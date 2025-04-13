import time

from selenium import webdriver
import allure
import pytest
@allure.title("verify the title of the vwo.com is as expected")
@pytest.mark.regression
def test01_vwo_login():
    driver=webdriver.Chrome()
    # This code is translated to API request
    # Post Request- browser driver(server)
    # where it will create a session or fresh copy browser (chrome)
    # session id- 16 digit (jggj78gh6ffd2345y) will be created
    driver.get("https://app.vwo.com")
    time.sleep(15)
    # print(driver.session_id)
    print(driver.title)
    assert driver.title == "Login - VWO"