from typing import List
from dsb_client import DSBClient, LoginReturnDataDTO, MessageDTO
import asyncio

client = DSBClient(host='http://localhost:3001')

identity_token = 'eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJkaWQ6ZXRocjoweDM3ZDM3YjEwZDExODZhRTQxNzM3RDM4YjJkQkM1Qzg4MzE2YzlGQmQiLCJjbGFpbURhdGEiOnsiYmxvY2tOdW1iZXIiOjk5OTk5OTk5OTk5OX19.MHhiZWU0ODJhZGI2NzYwZWQyZjAyMTYwZGYxMGMxZjJiMDE5NzRmZGRkZDE0YmFkZmEyMWIyNDliZGU5NGNmZmUwMjY3N2RkZmEwYzhhODA0NDIyYTBmOTMyYTA5NjlkMWNiNzA1ZjYyN2NjMDg1NWRjNjYzYWQ2ZThkNWZiOTc1NjFi'

health = asyncio.run(client.health.check())
print('Client is', health.status)

login:LoginReturnDataDTO = asyncio.run(client.auth.login(identity_token=identity_token))

client.update(token=login.token)
print('Logged in')

messages:List[MessageDTO] = asyncio.run(client.message.pull(fqcn='test.channels.testapp.apps.testorganization.iam.ewc'))
print(messages)
