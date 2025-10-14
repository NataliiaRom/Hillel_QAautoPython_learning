from selenium.webdriver.common.by import By


class HomePageLocators:
    signup_button = (By.CSS_SELECTOR, ".btn-primary")
    registration_form = (By.CSS_SELECTOR, ".modal-content")
    name = (By.XPATH, '//input[@name="name"]')
    last_name = (By.XPATH, '//input[@name="lastName"]')
    email = (By.XPATH, '//input[@name="email"]')
    password = (By.XPATH, '//input[@name="password"]')
    repeat_pwd = (By.XPATH, '//input[@name="repeatPassword"]')
    submit_btn = (By.CSS_SELECTOR, '.modal-footer .btn-primary')
    alert_user_exists = (By.CSS_SELECTOR, '.alert-danger')
    alert_invalid_field_value = (By.CSS_SELECTOR, '.invalid-feedback')

class MyProfilePageLocators:
    my_profile_menu = (By.ID, "userNavDropdown")
