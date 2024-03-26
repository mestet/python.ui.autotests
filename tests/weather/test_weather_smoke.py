import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


@allure.id(1)
@allure.story("Weather testing")
@allure.feature("test_sahara_weather Sahara")
@allure.testcase("Check if it warm weather in the Eye of the Sahara")
def test_sahara_weather(chrome):
    chrome.get("https://www.accuweather.com/")

    # agreeing with cookies policy
    try:
        cookies = chrome.find_element(By.XPATH, '//div[@class="fc-consent-root"]')
        cookies.find_element(By.XPATH, '//button[@aria-label="Consent"]').click()
    except NoSuchElementException:
        print("No cookies message")

    search_input = chrome.find_element(By.XPATH, '//input[@name="query" and @class="search-input"]')
    search_input.send_keys("21.124, -11.404\n")  # Eye of the Sahara desert coords

    weather_card = '//div[@class="cur-con-weather-card__body"]'
    with allure.step(f"Waiting for element: {weather_card}"):
        weather_container = WebDriverWait(chrome, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, weather_card))
        )
    spaced_content = weather_container.find_element(By.XPATH, '//div[@class="temp"]')

    temp_text = spaced_content.text  # Two last symbols is about grad (ex = '31°C')
    assert temp_text[-2:] == "°C"
    assert int(temp_text[:-2]) > 25


@allure.id(2)
@allure.story("Weather testing")
@allure.feature("test_antarctic_weather Antarctic")
@allure.testcase("Check if it warm weather in the Antarctic")
def test_antarctic_weather(chrome):
    chrome.get("https://www.accuweather.com/")

    # agreeing with cookies policy
    try:
        cookies = chrome.find_element(By.XPATH, '//div[@class="fc-consent-root"]')
        cookies.find_element(By.XPATH, '//button[@aria-label="Consent"]').click()
    except NoSuchElementException:
        print("No cookies message")

    search_input = chrome.find_element(By.XPATH, '//input[@name="query" and @class="search-input"]')
    search_input.send_keys("McMurdo Station, AQ\n")  # Eye of the Sahara desert coords

    with allure.step(f"Waiting for element"):
        weather_container = WebDriverWait(chrome, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//div[@class="cur-con-weather-card__body"]'))
        )
    spaced_content = weather_container.find_element(By.XPATH, '//div[@class="temp"]')

    temp_text = spaced_content.text  # Two last symbols is about grad (ex = '31°C')
    assert temp_text[-2:] == "°C"
    assert int(temp_text[:-2]) < -10
