import time
import allure
import pickle
from faker import Faker
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from metaclasses.meta_locator import MetaLocator

class UIHelper(metaclass=MetaLocator):

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 15, poll_frequency=1)
        self.actions = ActionChains(self.driver)
        self.fake = Faker()
        self.EC = EC

    def open(self):
        self.driver.get(self._PAGE_URL)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self._PAGE_URL))

    def find(self, locator: tuple, element_name: str = None):
        return self.wait.until(EC.visibility_of_element_located(locator), f"{element_name} is not visibility")

    def find_all(self, locator: tuple, wait=False):
        if wait:
            return self.wait.until(EC.visibility_of_all_elements_located(locator))
        else:
            return self.driver.find_elements(*locator)

    def fill(self, locator: tuple, text: str):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator: tuple, element_name: str = None):
        return self.wait.until(EC.element_to_be_clickable(locator), message=f"{element_name} is not clickable").click()

    def screenshot(self, name: str =time.time()):
        """
        This method takes a screenshot from browser
        :param name: name of screenshot
        :return: None
        """
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    def wait_for_invisibility(self, locator: tuple, message: str = None):
        return self.wait.until(EC.invisibility_of_element(locator), message=message)

    def save_cookies(self, cookies_name="temp-cookies"):
        pickle.dump(self.driver.get_cookies(), open(f"cookies/{cookies_name}.pkl", "wb"))

    def load_cookies(self, cookies_name: str=None):
        cookies = pickle.load(open(f"cookies/{cookies_name}.pkl", "rb"))
        self.driver.delete_all_cookies()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def scroll_by(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0)")

    def scroll_to_element(self, locator):
        self.actions.scroll_to_element(self.find(locator))
        self.driver.execute_script("""
        window.scrollTo({
            top: window.scrollY + 500,
        });
        """)

    def switch_to_iframe(self, locator: tuple, message: str = None):
        self.wait.until(self.EC.frame_to_be_available_and_switch_to_it(locator), message=message)

    def switch_to_default_frame(self):
        self.default_content = self.driver.switch_to.default_content()
        self.wait.until(self.EC.frame_to_be_available_and_switch_to_it(self.default_content),
                        "Default content frame unavailable")

