import unittest

from playwright.sync_api import sync_playwright


class TestRedbusBooking(unittest.TestCase):
    def setUp(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://www.redbus.in/")

    def test_calender(self):
        self.page.locator("//*[text()='Date']").click()
        self.page.wait_for_selector("//div[text()='Mar']", state="attached")
        next_arrow_click = 12
        while next_arrow_click > 0:
            try:
                current_month = self.page.locator(
                    "//div[contains(@class,'DayNavigator')][2]"
                ).inner_text()
                if "Apr" in current_month:
                    self.page.click(
                        "//span[contains(@class, 'DayTiles__CalendarDaysSpan') and text()='19']"
                    )
                    break
            except Exception as e:
                next_arrow_click -= 1
                self.page.click(
                    "//div[contains(@class, 'DayNavigator')]/*[name()='svg']"
                )

    def tearDown(self):
        self.page.close()
        self.browser.close()
        self.playwright.stop()
