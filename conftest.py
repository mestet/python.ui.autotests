from collections import namedtuple

import pytest
from pydantic import BaseSettings

from utils.browser import BrowserChrome


class Settings(BaseSettings):
    chrome_host: str = 'localhost'
    chrome_port: int = 4444


settings = Settings()


@pytest.fixture
def chrome_browser():
    browser = BrowserChrome(
        remote_host=settings.chrome_host,
        remote_port=settings.chrome_port
    )
    yield browser.driver
    browser.driver.quit()


@pytest.fixture
def autotest_user():
    user = namedtuple('TestUser', ['email', 'password'])
    user.email = 'autotest@lucky-team.pro'
    user.password = 'd2f0fd3eef'
    return user
