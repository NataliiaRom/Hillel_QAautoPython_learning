import pytest

from lesson24.logging_config import logger


class TestAuth:
    # TEST POSITIVE AUTH FOR DIFF CREDENTIALS
    users = {
        "test_user": "test_pass",
    }

    # passing users data (as a list) to requests.param
    @pytest.mark.parametrize("establishing_cars_auth_check", [[user, pwd] for user, pwd in users.items()],
                             indirect=True)
    def test_user_authentication_positive(self, establishing_cars_auth_check, request):
        logger.info(f"\t### PERFORMING {request.node.name} ###")

        token = establishing_cars_auth_check
        assert token, logger.error("Authentication failed. No token received or wrong credentials.")

    # TEST NEGATIVE AUTH FOR DIFF CREDENTIALS
    users = {
        "admin": "admin",
        None: None
    }

    # passing users data (as a list) to requests.param
    @pytest.mark.parametrize("establishing_cars_auth_check", [[user, pwd] for user, pwd in users.items()],
                             indirect=True)
    def test_user_authentication_negative(self, establishing_cars_auth_check, request):
        logger.info(f"\t### PERFORMING {request.node.name} ###")

        token = establishing_cars_auth_check
        assert not token, logger.error("User is authenticated. This behavior is not expected.")
