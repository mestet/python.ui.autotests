import pytest
from pydantic_settings import BaseSettings

from utils.browser import Chrome, HeadlessFirefox


class Settings(BaseSettings):
    selenium_host: str = 'localhost'  # 'selenium__standalone-chrome'
    selenium_port: int = 4444


settings = Settings()


@pytest.fixture
def chrome():
    browser = Chrome(
        remote_host=settings.selenium_host,
        remote_port=settings.selenium_port
    )
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def headless_firefox():
    browser = HeadlessFirefox(
        remote_host=settings.selenium_host,
        remote_port=settings.selenium_port
    )
    yield browser
    browser.quit()
