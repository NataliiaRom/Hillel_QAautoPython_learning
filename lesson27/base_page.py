from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.url = None

    def open_page(self, url=None):
        url = url or self.url
        self._driver.get(url)

    def _input_field(self, locator):  # locator = tuple(type_of_selector, selector)
        return WebDriverWait(self._driver, timeout=2).until(
            EC.presence_of_element_located(locator))

    def _button(self, locator):  # locator = tuple(type_of_selector, selector)
        return WebDriverWait(self._driver, timeout=2).until(
            EC.element_to_be_clickable(locator))

    def _inactive_button(self, locator):
        return WebDriverWait(self._driver, timeout=2).until_not(
            EC.element_to_be_clickable(locator)
        )

    def _present_element(self, locator):
        return WebDriverWait(self._driver, timeout=2).until(
            EC.presence_of_element_located(locator)
        )
