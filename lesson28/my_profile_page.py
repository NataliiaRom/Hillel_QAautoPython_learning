from lesson28.base_page import BasePage
from settings import settings
from lesson28.locators import MyProfilePageLocators

class MyProfilePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver=driver)
        self.url = settings.qaauto2_my_profile_page
        self.locators = MyProfilePageLocators()

    def my_profile_menu(self):
        return self._present_element(self.locators.my_profile_menu)

