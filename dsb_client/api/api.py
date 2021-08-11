from dsb_client.api.crypto import Crypto
from dsb_client.swagger_client.api.channel_api import ChannelApi
from dsb_client.api.channel import Channel
from dsb_client.api.health import Health
from dsb_client.swagger_client.api.health_api import HealthApi
from dsb_client.api.message import Message
from dsb_client.api.auth import Auth
from dsb_client.swagger_client.api.message_api import MessageApi
from dsb_client.swagger_client.api_client import ApiClient
from dsb_client.swagger_client.api.auth_api import AuthApi
from dsb_client.swagger_client.configuration import Configuration

class DSBClient:
    auth:Auth
    health:Health
    message:Message
    channel:Channel
    crypto:Crypto

    def __init__(self, host:str) -> None:
        config = Configuration()
        config.host = host
        self.__client = ApiClient(configuration=config)

        auth_api = AuthApi(api_client=self.__client)
        health_api = HealthApi(api_client=self.__client)
        message_api = MessageApi(api_client=self.__client)
        channel_api = ChannelApi(api_client=self.__client)

        self.auth = Auth(auth_api=auth_api)
        self.health = Health(health_api=health_api)
        self.message = Message(message_api=message_api)
        self.channel = Channel(channel_api=channel_api)

        self.crypto = Crypto()

    def update(self, token:str) -> None:
        self.__client.set_default_header('Authorization', f'Bearer {token}')
