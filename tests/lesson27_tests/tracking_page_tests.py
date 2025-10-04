def test_tracking_page_is_open(driver, tracking_page):
    tracking_page.open_page()
    assert tracking_page.track_form().is_displayed(), \
        "Error displaying a page. Tracking form is not visible."


def test_too_short_tracking_number(driver, tracking_page):
    tn = "123004"
    tracking_page.tracking_number_insert(tn)
    tracking_page.inactive_search_btn()


def test_not_existing_tracking_number(driver, tracking_page):
    tn = "12300471653200"
    tracking_page.tracking_number_search(tn)
    assert "Ми не знайшли посилку за таким номером" in tracking_page.tracking_err_text().text


def test_existing_tracking_number(driver, tracking_page):
    tn = "20400471653273"
    tracking_page.tracking_number_search(tn)
    assert "Зараз:" in tracking_page.tracking_info_text().text
