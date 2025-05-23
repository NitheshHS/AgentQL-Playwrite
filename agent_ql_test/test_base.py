import agentql
import pytest
from playwright.sync_api import sync_playwright
from pygments.lexer import default

from utilities.config_reader import ConfigReader


class TestBase:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        config = ConfigReader()
        with sync_playwright() as playwrite, playwrite.chromium.launch(
            headless=bool(not config.get("Settings", "headless", default=False))
        ) as browser:
            page = agentql.wrap(browser.new_page())
            page.goto(config.get("Application", "URL"))
            yield page
            browser.close()
