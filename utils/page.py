import allure
from selenium.common.exceptions import NoSuchElementException

# todo move to browser class
def find_element(driver, locator_type, locator):
    with allure.step(f'Searching for element {locator_type}: {locator}'):
        try:
            return driver.find_element(locator_type, locator)
        except NoSuchElementException as e:
            raise AssertionError(e, f'Failed to find element')
