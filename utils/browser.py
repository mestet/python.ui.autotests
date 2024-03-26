import allure

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class AlluredBrowser(WebDriver):
    @allure.step("GET url '{url}'")
    def get(self, url):
        return super().get(url)

    @allure.step("Find element '{value}' by {by}")
    def find_element(self, by: str, value: str = None):
        return super().find_element(by=by, value=value)


class Chrome(AlluredBrowser):

    def __init__(self, remote_host, remote_port):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--ignore-ssl-errors=yes')
        chrome_options.add_argument('--ignore-certificate-errors')

        super().__init__(
            command_executor=f"http://{remote_host}:{remote_port}/wd/hub",
            options=chrome_options
        )


class HeadlessFirefox(AlluredBrowser):
    def __init__(self, remote_host, remote_port):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument('--ignore-ssl-errors=yes')
        firefox_options.add_argument('--ignore-certificate-errors')

        super().__init__(
            command_executor=f"http://{remote_host}:{remote_port}/wd/hub",
            options=firefox_options
        )
