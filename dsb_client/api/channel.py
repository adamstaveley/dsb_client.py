from dsb_client.swagger_client.api import ChannelApi
from dsb_client.swagger_client.models import CreateChannelDto

class Channel:
    def __init__(self, channel_api:ChannelApi) -> None:
        self.channel = channel_api

    async def create(self, fqcn:str):
        body = CreateChannelDto(fqcn=fqcn)
        thread = self.channel.channel_controller_create(body=body, async_req=True)
        return thread.get()
