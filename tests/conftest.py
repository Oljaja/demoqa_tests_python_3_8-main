import pytest
from selene.support.shared import browser


@pytest.fixture()
def window_size():
    browser.config.window_width = 1024
    browser.config.window_height = 1024






