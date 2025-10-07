import random

import pytest

### TEST successful registration
numb = random.choice(range(1, 1000))
frozen_password = "anna" + str(numb) + "@from.el"

test_data = {
    "name": "Anna",
    "last_name": "Elza",
    "email": frozen_password,
    "password": "1Qaz2wsx",
    "repeat_password": "1Qaz2wsx"
}

test_data_for_test = [(test_data["name"], test_data["last_name"], test_data["email"], test_data["password"],
                       test_data["repeat_password"])]


@pytest.mark.parametrize("name,last_name,email,password,repeat_password", test_data_for_test)
def test_successful_registration(driver, qaauto2_homepage, myprofile_page, name, last_name, email, password,
                                 repeat_password):
    qaauto2_homepage.registration(
        name, last_name, email, password, repeat_password
    )

    assert myprofile_page.my_profile_menu().is_displayed()


### TEST user already exists ###
@pytest.mark.parametrize("name,last_name,email,password,repeat_password", test_data_for_test)
def test_user_already_exists_registration(driver, qaauto2_homepage, myprofile_page, name, last_name, email, password,
                                          repeat_password):
    qaauto2_homepage.registration(
        name, last_name, email, password, repeat_password
    )
    assert qaauto2_homepage.alert_user_exists().is_displayed()
    assert "User already exists" in qaauto2_homepage.alert_user_exists().text
