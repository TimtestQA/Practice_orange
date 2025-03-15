from pages.login_page import LoginPage

class BaseTest:


    def setup_method(self):
        self.login_page = LoginPage(self.driver)

