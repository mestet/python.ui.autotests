import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


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
    login_button = remote_driver.find_element(By.CLASS_NAME, "header__link--secondary")
    assert login_button is not None
    login_button.click()
    assert remote_driver.current_url.startswith("https://my.luckyfeed.pro/login")


@allure.testcase("LuckyFeed login button")
def test_login_form(remote_driver):
    remote_driver.get("https://my.luckyfeed.pro/login")
    login_field = remote_driver.find_element('xpath',
                                             '//*[@id="__layout"]/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/input')
    password_field = remote_driver.find_element('xpath',
                                                '//*[@id="__layout"]/div/div[1]/div[2]/div/div/div/form/div[2]/div/div/input')

    submit_button = remote_driver.find_element('xpath',
                                               '//*[@id="__layout"]/div/div[1]/div[2]/div/div/div/form/div[4]/button')

    # todo parametrize
    login_field.send_keys("autotest@lucky-team.pro")
    password_field.send_keys("d2f0fd3eef")
    submit_button.click()
    time.sleep(10) # todo do not wait or wait less
    assert remote_driver.current_url.startswith("https://my.luckyfeed.pro/news")
