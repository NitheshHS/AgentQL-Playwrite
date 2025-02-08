from agent_ql_test.test_base import TestBase
from page.LoginPage import LoginPage


class TestLogin(TestBase):

    def test_login_sauce(self, setup_and_teardown):
        page = setup_and_teardown
        login_page=LoginPage(page)
        login_page.login('standard_user', 'secret_sauce')