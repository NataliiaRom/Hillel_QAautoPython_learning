import pytest
from lesson11.homework_11 import log_event

log_file = "login_system.log"
user = "Nata"

def clear_logfile_input(file_path):
    open(file_path, 'w').close()

def user_login_events_handler(file_path,name,user_status):
    with open(log_file) as log:
        lines = log.readlines()  # to get an output as a list of lines
        # checking log info corresponds the last line only
        assert lines[-1].strip().endswith(f'Login event - Username: {name}, Status: {user_status}'), \
            f"There is no event for {name} with {user_status} login. Test failed"
        print(f"log includes info for {name} with {user_status} login")


class TestUserLogin:

    def test_successful_login(self):
        # clear_logfile_input(log_file)  # not necessary, because I check the correspondence to the last line only
        status = "success"
        log_event(user,status)
        user_login_events_handler(log_file,user,status)

    def test_expired_login(self):
        # clear_logfile_input(log_file)  # not necessary, because I check the correspondence to the last line only
        status = "expired"
        log_event(user,status)
        user_login_events_handler(log_file,user,status)

    def test_weird_login(self):
        # clear_logfile_input(log_file)  # not necessary, because I check the correspondence to the last line only
        status = "lalala"
        log_event(user,status)
        user_login_events_handler(log_file,user,status)

