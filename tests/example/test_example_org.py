import allure
from selenium.webdriver.common.by import By


@allure.id(42)
@allure.testcase('Check if github corner is available')
def test_httpbin_org(chrome):
    chrome.get('https://eu.httpbin.org/')
    element = chrome.find_element(By.XPATH, '//*[@class="github-corner"]')
    assert element.is_enabled()
