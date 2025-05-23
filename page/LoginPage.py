from agentql.ext.playwright.async_api.response_proxy import AQLResponseProxy

from utilities.ui_interactions import UiInteractions


class LoginPage(UiInteractions):
    def __init__(self, page):
        super().__init__(page)
        query_login_elements = """{
                                        username,
                                        password,
                                        login
                                        }"""
        self._elements = page.query_elements(query_login_elements)
        self._user_name = self._elements.username
        self._password = self._elements.password
        self._login_btn = self._elements.login
        self.page = page

    def login(self, username, password):
        self.fill_element(self._user_name, username)
        self.fill_element(self._password, password)
        self.click_on_element(self._login_btn)
        assert self.page.title() == "Swag Labs"
