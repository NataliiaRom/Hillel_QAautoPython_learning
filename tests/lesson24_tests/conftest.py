from urllib.parse import urljoin
import requests
import pytest

from lesson24.user_auth_basic import UsersAuth

@pytest.fixture()
def establishing_cars_auth_check(request):
    print(f"\n###STARTING the connection check - {request.node.name}###\n")
    user, pwd = request.param # unpacking usr and pwd from the passed list

    # initializing auth object
    auth = UsersAuth(user, pwd)
    token = auth.auth()

    yield token

    print(f"\n### FINISHING connection check - {request.node.name}\n###")
    auth.session.close()

@pytest.fixture(scope = "class")
def cars_auth(request):
    print(f"\n###ESTABLISHING CONNECTION with cars APP - {request.node.name} ###\n")
    user = "test_user"
    pwd = "test_pass"

    # getting connection details
    auth = UsersAuth(user, pwd)
    BASE_URL = auth.BASE_URL
    session = auth.session
    token = auth.auth()


    yield token,session,BASE_URL

    print(f"\n###CLOSING CONNECTION to the cars App - {request.node.name}\n###")
    auth.session.close()

@pytest.fixture()
def get_cars(request,cars_auth):
    if request.param:
        key,value = request.param
        params = {key: value}
    else:
        params = None

    token,session,BASE_URL = cars_auth

    cars_endpoint = urljoin(BASE_URL, "cars")
    headers = {'Authorization': f'Bearer {token}'}

    response = session.get(cars_endpoint, headers=headers, params=params)

    yield response
