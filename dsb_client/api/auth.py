from typing import Coroutine
from swagger_client.api.auth_api import AuthApi
from swagger_client.models import LoginDataDTO, LoginReturnDataDTO

class Auth:
    def __init__(self, auth_api:AuthApi):
        self.auth = auth_api

    async def login(self, identity_token:str):
        body = LoginDataDTO(identity_token=identity_token)
        thread = self.auth.auth_controller_login(body=body, async_req=True)
        return thread.get()
