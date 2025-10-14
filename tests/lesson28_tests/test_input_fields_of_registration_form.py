import pytest

### TEST mandatory fields ####
registration_data_sets = [
    {
        "name": "",
        "last_name": "",
        "email": "",
        "password": "",
        "repeat_password": ""
    },
    {
        "name": "Anna",
        "last_name": "Elza",
        "email": "",
        "password": "1Qaz2wsx",
        "repeat_password": "1Qaz2wsx"
    },
    {
        "name": "",
        "last_name": "Elza",
        "email": "an1@from.el",
        "password": "1Qaz2wsx",
        "repeat_password": "1Qaz2wsx"
    }
]
# list of tuples (name, last_name, email, password, repeat_password) for parametrize
registration_data_sets_for_tests = [
    (data["name"], data["last_name"], data["email"], data["password"], data["repeat_password"])
    for data in registration_data_sets
]


@pytest.mark.parametrize("name,last_name,email,password,repeat_password", registration_data_sets_for_tests)
def test_all_mandatory_fields_are_filled(driver, qaauto2_homepage, name, last_name, email, password, repeat_password):
    qaauto2_homepage.wrong_input_values_insert(
        name, last_name, email, password, repeat_password
    )

    # Empty fields count
    required_fields_count = 0
    for value in [name, last_name, email, password, repeat_password]:
        if value == "":
            required_fields_count += 1

    for i in qaauto2_homepage.print_alert_messages():
        assert "required" in i
    assert required_fields_count == len(qaauto2_homepage.print_alert_messages())
    qaauto2_homepage.submit_btn_inactive()


### TEST name/last name include only alphabetical chars ###
def test_alerts_by_wrong_values_at_registration(driver, qaauto2_homepage):
    name = "an1"
    last_name = "fro1"
    email = "an1.from.el"
    password = "a2wsx"
    repeat_password = password + "1"
    qaauto2_homepage.wrong_input_values_insert(
        name, last_name, email, password, repeat_password
    )
    assert 5 == len(qaauto2_homepage.print_alert_messages())
    qaauto2_homepage.submit_btn_inactive()


####TEST passwords do not match ###
def test_passwords_not_match(driver, qaauto2_homepage):
    password = "1Qaz2wsx"
    repeat_password = password + "abc"
    qaauto2_homepage.compare_two_password_fields(password, repeat_password)
    for i in qaauto2_homepage.alert_invalid_field_values():
        assert "do not match" in i.text


### TEST password requirements do not match ###
passwords_for_test = [("1oaz2wsx", "1oaz2wsx"), ("1az2wsx", "1az2wsx"), ("fght", "fght"),
                      ("12345rfvbgtyhnmj", "12345rfvbgtyhnmj")]


@pytest.mark.parametrize("password,repeat_password", passwords_for_test)
def test_catch_wrong_pass(driver, qaauto2_homepage, password, repeat_password):
    qaauto2_homepage.compare_two_password_fields(password, repeat_password)
    for i in qaauto2_homepage.alert_invalid_field_values():
        assert "Password has to be" in i.text
