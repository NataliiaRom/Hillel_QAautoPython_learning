import pytest
# from selenium.webdriver import Chrome
from selenium.webdriver.edge.webdriver import WebDriver

from lesson27.tracking_page import TrackingPage


@pytest.fixture
def driver():
    driver = WebDriver()
    yield driver
    driver.close()

@pytest.fixture
def tracking_page(driver):
    tracking_page=TrackingPage(driver)
    tracking_page.open_page()
    return tracking_page