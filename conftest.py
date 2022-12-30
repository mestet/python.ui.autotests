from collections import namedtuple

import pytest


@pytest.fixture
def autotest_user():
    user = namedtuple('TestUser', ['email', 'password'])
    user.email = 'autotest@lucky-team.pro'
    user.password = 'd2f0fd3eef'
    return user
