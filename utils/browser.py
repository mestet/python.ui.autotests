from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BrowserChrome:
    driver: WebDriver

    def __init__(self, remote_host, remote_port):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Remote(
            command_executor=f"{remote_host}:{remote_port}/wd/hub",
            options=options
        )

    def __del__(self):
        self.driver.quit()
