import pytest
from playwright.sync_api import sync_playwright

from utilities.ui_interactions import UiInteractions


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    # Check if test failed
    if result.when == "call" and result.failed:
        # Get the "page" fixture if used in the test
        page = item.funcargs.get("page", None)
        if page:
            UiInteractions(page).screenshot(item.name)
