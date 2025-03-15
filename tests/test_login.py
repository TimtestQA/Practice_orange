import time

import allure
from base.base_test import BaseTest
import pytest

class TestLogin(BaseTest):

    @pytest.mark.smoke
    def test_login(self):
        self.login_page.open()
        self.login_page.enter_login("Admin")
        self.login_page.enter_password("admin123")
        self.login_page.click_submit()
        time.sleep(3)