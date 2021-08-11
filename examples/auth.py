from typing import List
from dsb_client.swagger_client.models.message_dto import MessageDTO
from dsb_client.swagger_client import ApiClient, AuthApi, MessageApi, Configuration
from dsb_client.swagger_client.models import LoginDataDTO

config = Configuration()
config.host = 'http://localhost:3001' # message broker

client = ApiClient(configuration=config)
auth = AuthApi(api_client=client)

loginBody = LoginDataDTO(
    identity_token='eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJkaWQ6ZXRocjoweDM3ZDM3YjEwZDExODZhRTQxNzM3RDM4YjJkQkM1Qzg4MzE2YzlGQmQiLCJjbGFpbURhdGEiOnsiYmxvY2tOdW1iZXIiOjk5OTk5OTk5OTk5OX19.MHhiZWU0ODJhZGI2NzYwZWQyZjAyMTYwZGYxMGMxZjJiMDE5NzRmZGRkZDE0YmFkZmEyMWIyNDliZGU5NGNmZmUwMjY3N2RkZmEwYzhhODA0NDIyYTBmOTMyYTA5NjlkMWNiNzA1ZjYyN2NjMDg1NWRjNjYzYWQ2ZThkNWZiOTc1NjFi'
)

login = auth.auth_controller_login(body=loginBody)


# print('get', config.auth_settings().get('access-token'))

msg = MessageApi(api_client=client)
msg.api_client.set_default_header("Authorization", f'Bearer {login.token}')

sent:List[MessageDTO] = msg.message_controller_get_new_from_channel(fqcn='test.channels.testapp.apps.testorganization.iam.ewc')

print(sent[0].id)
