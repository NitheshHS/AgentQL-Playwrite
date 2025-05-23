from playwright.sync_api import Page, Route


def test_mock(page: Page):
    def handle(route: Route):
        json = [{"name": "nithesh", "id": 18}, {"name": "xyz", "id": 19}]
        route.fulfill(json=json)

    page.route("*/**/api/v1/fruits", handle)

    page.goto("https://demo.playwright.dev/api-mocking")

    page.pause()
