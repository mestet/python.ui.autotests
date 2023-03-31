import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from utils.page import find_element


@allure.testcase("LuckyFeed login button")
def test_login_smoke(chrome_browser):
    chrome_browser.get("https://weather.com//")
    search_input = chrome_browser.find_element(By.ID, "LocationSearch_input")
    assert search_input is not None
    search_input


@allure.testcase("LuckyFeed login button")
def test_login_form(chrome_browser, autotest_user):
    chrome_browser.get("https://my.luckyfeed.pro/login")
    login_field = find_element(chrome_browser, By.XPATH, '//input[@type="email"]')
    password_field = find_element(chrome_browser, By.XPATH, '//input[@type="password"]')
    submit_button = find_element(chrome_browser, By.XPATH, '//button[@type="submit"]')

    login_field.send_keys("autotest@testmail.com")
    password_field.send_keys("password")
    submit_button.click()
    user_email = WebDriverWait(chrome_browser, 30).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//div[@class="lna-profile__avatar-email"]'))
    )

    assert user_email.text == 'autotest@lucky-team.pro'
