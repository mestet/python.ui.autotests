import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.page import find_element


# todo separate module for browser with allure steps
@pytest.fixture
def remote_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=options
    )
    yield driver
    driver.close()
    driver.quit()


@allure.testcase("LuckyFeed login button")
def test_login_smoke(remote_driver):
    remote_driver.get("https://luckyfeed.pro/")
    find_element(remote_driver, By.CLASS_NAME, 'header__link--secondary')
    login_button = remote_driver.find_element(By.CLASS_NAME, "header__link--secondary")
    assert login_button is not None
    login_button.click()
    assert remote_driver.current_url.startswith("https://my.luckyfeed.pro/login")


@allure.testcase("LuckyFeed login button")
def test_login_form(remote_driver, autotest_user):
    remote_driver.get("https://my.luckyfeed.pro/login")
    login_field = find_element(remote_driver, 'xpath', '//input[@type="email"]')
    password_field = find_element(remote_driver, 'xpath', '//input[@type="password"]')
    submit_button = find_element(remote_driver, 'xpath', '//button[@type="submit"]')

    # todo parametrize
    login_field.send_keys("autotest@lucky-team.pro")
    password_field.send_keys("d2f0fd3eef")
    submit_button.click()
    time.sleep(10) # todo do not wait or wait less

    user_email = find_element(remote_driver, 'xpath', '//div[@class="lna-profile__avatar-email"]')
    assert user_email.text == 'autotest@lucky-team.pro'
