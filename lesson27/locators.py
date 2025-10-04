from selenium.webdriver.common.by import By


class TrackingPageLocators:
    tracking_field_input = (By.CSS_SELECTOR, ".track__form-group-input")
    search_btn = (By.CSS_SELECTOR, ".track__form-group-btn")
    err_msg_field = (By.ID, "np-number-input-desktop-message-error-message")
    tracking_err_msg = (By.XPATH, "//div[contains(@class,'track__form-message')]/span")
    tracking_info_msg = (By.CSS_SELECTOR, ".header__status-header")
    track_form = (By.CSS_SELECTOR, ".track__form")