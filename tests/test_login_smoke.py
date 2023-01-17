import allure
from selenium.webdriver.common.by import By

from utils.page import find_element


@allure.testcase("LuckyFeed login button")
def test_login_smoke(chrome_browser):
    chrome_browser.get("https://luckyfeed.pro/")
    find_element(chrome_browser, By.CLASS_NAME, 'header__link--secondary')
    login_button = chrome_browser.find_element(By.CLASS_NAME, "header__link--secondary")
    assert login_button is not None
    login_button.click()
    assert chrome_browser.current_url.startswith("https://my.luckyfeed.pro/login")


# @allure.testcase("LuckyFeed login button")
# def test_login_form(chrome_browser, autotest_user):
#     chrome_browser.get("https://my.luckyfeed.pro/login")
#     login_field = find_element(chrome_browser, 'xpath', '//input[@type="email"]')
#     password_field = find_element(chrome_browser, 'xpath', '//input[@type="password"]')
#     submit_button = find_element(chrome_browser, 'xpath', '//button[@type="submit"]')
#
#     # todo parametrize
#     login_field.send_keys("autotest@lucky-team.pro")
#     password_field.send_keys("d2f0fd3eef")
#     submit_button.click()
#     time.sleep(10)  # todo do not wait or wait less ex WebDriverWait(driver, 30).until()
#
#     user_email = find_element(chrome_browser, 'xpath', '//div[@class="lna-profile__avatar-email"]')
#     assert user_email.text == 'autotest@lucky-team.pro'
