from dsb_client.swagger_client.api.message_api import MessageApi
from dsb_client.swagger_client.models import MessageDTO

class Message:
    def __init__(self, message_api:MessageApi) -> None:
        self.message = message_api

    async def send(self, data:MessageDTO):
        thread = self.message.message_controller_publish(body=data, async_req=True)
        return thread.get()

    async def pull(self, fqcn:str, amount:int=1):
        thread = self.message.message_controller_get_new_from_channel(fqcn=fqcn, amount=amount, async_req=True)
        return thread.get()
