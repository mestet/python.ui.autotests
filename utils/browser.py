from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BrowserChrome:
    driver: WebDriver

    def __init__(self, remote_host, remote_port):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--ignore-ssl-errors=yes')
        chrome_options.add_argument('--ignore-certificate-errors')

        self.driver = webdriver.Remote(
            command_executor=f"http://{remote_host}:{remote_port}/wd/hub",
            options=chrome_options
        )
