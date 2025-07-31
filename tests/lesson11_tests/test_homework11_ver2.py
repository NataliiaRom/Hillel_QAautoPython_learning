import pytest
from lesson11.homework_11 import log_event

log_file = "login_system.log"

def clear_logfile_input(file_path):
    open(file_path, 'w').close()

@pytest.mark.parametrize('user,status,log_msg',[
    ("Nata","success","Login event - Username: Nata, Status: success"),
    ("Peter", "expired", "Login event - Username: Peter, Status: expired"),
    ("John", "lalala", "Login event - Username: John, Status: lalala")
])
def test_user_login(user,status,log_msg):
    clear_logfile_input(log_file) # clearing the log_file content
    log_event(user,status) # launching event
     #reading log_file content
    with open(log_file,'r') as log:
        content = log.read()
    # checking the log file includes the necessary log event
    assert log_msg in content, f"The event '{status}' for {user} was not logged into a file."
