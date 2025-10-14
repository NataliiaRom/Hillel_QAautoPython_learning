from lesson28.base_page import BasePage
from lesson28.locators import HomePageLocators
from settings import settings


class QaAuto2HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = settings.qaauto2_url
        self.locators = HomePageLocators()

    def sign_up_btn(self):
        return self._button(self.locators.signup_button)

    def sign_up_btn_click(self):
        return self.sign_up_btn().click()

    def registration_form(self):
        return self._present_element(self.locators.registration_form)

    def name_field(self):
        return self._field(self.locators.name)

    def name_field_insert_value(self, name):
        self.name_field().click()
        self.name_field().send_keys(name)
        return self

    def last_name_field(self):
        return self._field(self.locators.last_name)

    def last_name_field_insert_value(self, last_name):
        self.last_name_field().click()
        self.last_name_field().send_keys(last_name)
        return self

    def email_field(self):
        return self._field(self.locators.email)

    def email_field_insert_value(self, email):
        self.email_field().click()
        self.email_field().send_keys(email)
        return self

    def password_field(self):
        return self._field(self.locators.password)

    def password_field_insert_value(self, password):
        self.password_field().click()
        self.password_field().send_keys(password)
        return self

    def repeat_password_field(self):
        return self._field(self.locators.repeat_pwd)

    def repeat_password_field_insert_value(self, repeat_password):
        self.repeat_password_field().click()
        self.repeat_password_field().send_keys(repeat_password)
        return self

    def compare_two_password_fields(self, password, repeat_password):
        self.sign_up_btn_click()
        self.password_field_insert_value(password)
        self.repeat_password_field_insert_value(repeat_password)
        self.password_field().click()
        return self

    def submit_btn(self):
        return self._button(self.locators.submit_btn)

    def submit_btn_click(self):
        self.submit_btn().click()
        return self

    def submit_btn_inactive(self):
        return self._inactive_button(self.locators.submit_btn)

    def registration(self, name, last_name, email, password, repeat_password):
        self.sign_up_btn_click()
        self.name_field_insert_value(name)
        self.last_name_field_insert_value(last_name)
        self.email_field_insert_value(email)
        self.password_field_insert_value(password)
        self.repeat_password_field_insert_value(repeat_password)
        self.submit_btn_click()
        return self

    def wrong_input_values_insert(self, name, last_name, email, password, repeat_password):
        self.sign_up_btn_click()
        self.name_field_insert_value(name)
        self.last_name_field_insert_value(last_name)
        self.email_field_insert_value(email)
        self.password_field_insert_value(password)
        self.repeat_password_field_insert_value(repeat_password)
        self.password_field().click()
        return self

    def alert_user_exists(self):
        return self._present_element(self.locators.alert_user_exists)

    def alert_invalid_field_values(self):
        return self._alert_elt(self.locators.alert_invalid_field_value)

    def print_alert_messages(self):  # returns a list
        alerts = self.alert_invalid_field_values()
        alerts_text = []
        for alert in alerts:
            alerts_text.append(alert.text)
        return alerts_text
