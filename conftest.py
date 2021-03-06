import pytest
from translations import *


@pytest.fixture(scope='session')
def env(pytestconfig):
    env = pytestconfig.getoption("env")
    if env == 'eng':
        return trans['eng']
    else:
        return trans['rus']


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="eng", help="Set environment for starting tests")