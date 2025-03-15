from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class LoginPage(BasePage):
    _PAGE_URL = Links.LOGIN_PAGE

    _LOGIN_FIELD = ("xpath", "//input[@name='username']")
    _PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    _SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")

    @allure.step("Ввод логина")
    def enter_login(self,login):
        self.wait.until(EC.element_to_be_clickable(self._LOGIN_FIELD)).send_keys(login)
    @allure.step("Ввод пароля")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self._LOGIN_FIELD)).send_keys(password)
    @allure.step("Нажать войти")
    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self._LOGIN_FIELD)).click()




