from settings import settings
from .base_page import BasePage
from .locators import TrackingPageLocators


class TrackingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = settings.novaposhta_base_url
        self.locators = TrackingPageLocators()

    # locating input field
    def tracking_field_input(self):
        return self._input_field(self.locators.tracking_field_input)

    # locating active search button
    def active_search_btn(self):
       return self._button(self.locators.search_btn)

    # locating inactive search button
    def inactive_search_btn(self):
        return self._inactive_button(self.locators.search_btn)

    # inserting tracking number
    def tracking_number_insert(self, tracking_number):
        self.tracking_field_input().send_keys(tracking_number)
        return self

    # active search button onclick
    def click_search_btn(self):
        self.active_search_btn().click()
        return self

    # getting tracking info ERR msg text
    def tracking_err_text(self):
        return self._present_element(self.locators.tracking_err_msg)

    # getting tracking info INFO msg text
    def tracking_info_text(self):
        return self._present_element(self.locators.tracking_info_msg)

    # getting the info about the searched tracking number
    def tracking_number_search(self,tn):
        return self.tracking_number_insert(tn).click_search_btn()

    # getting tracking form: input_field + button
    def track_form(self):
        return self._present_element(self.locators.track_form)