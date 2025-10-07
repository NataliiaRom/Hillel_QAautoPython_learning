import pytest
from selenium.webdriver.edge.webdriver import WebDriver

from lesson28.qaauto2_homepage import QaAuto2HomePage
from lesson28.my_profile_page import MyProfilePage


@pytest.fixture()
def driver():
    driver = WebDriver()
    yield driver
    driver.quit()

# open initial page before the tests begin
@pytest.fixture()
def qaauto2_homepage(driver):
    qaauto2_homepage = QaAuto2HomePage(driver)
    qaauto2_homepage.open_page()
    return qaauto2_homepage

# open My Profile page
@pytest.fixture()
def myprofile_page(driver):
    myprofile_page =  MyProfilePage(driver)
    myprofile_page.open_page()
    return myprofile_page


