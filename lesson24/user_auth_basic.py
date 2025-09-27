import requests
from urllib.parse import urljoin

class UsersAuth:
    def __init__(self,user,pwd):
        self.user = user
        self.pwd = pwd
        self.session = requests.Session() # all the requests will go through the session
        self.BASE_URL = "http://127.0.0.1:8080"

    def auth(self):
        ## USER AUTHENTICATION ##
        auth_endpoint = urljoin(self.BASE_URL, "auth")
        response = self.session.post(auth_endpoint, auth=(self.user, self.pwd))
        # getting access token
        if response.status_code == 200:
            token = response.json().get('access_token')
        else:
            token = None
        return token