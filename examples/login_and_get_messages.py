from typing import List
from dsb_client import DSBClient, LoginReturnDataDTO, MessageDTO
import asyncio

# configure with your message broker host
client = DSBClient(host='http://localhost:3001')

# sign proof of DID ownership
# note! the DID should already have enroled in Switchboard to the "user" role
# see documentation about enrolment on https://github.com/energywebfoundation/dsb
identity_token = client.crypto.get_identity_token(
    did="did:ethr:0x37d37b10d1186aE41737D38b2dBC5C88316c9FBd",
    private_key='0xe2caca2e7c22fc5bf985cc6838e152753c52b925620bf2449e388c90e3d853f7')

# fetch health (note this unauthenticated)
# client methods that call a message broker endpoint are async
health = asyncio.run(client.health.check())
print('Client is', health.status)

# use the signed identity proof to login
login:LoginReturnDataDTO = asyncio.run(
    client.auth.login(identity_token=identity_token))

# in the login result we should get our JWT bearer auth token
# we update the client to use the new auth token
# note that token refresh is not handled by the client as of now
client.update(token=login.token)
print('Logged in')

# now that the client is authenticated, we can use the message broker to
# pub/sub to messages on a particular channel
messages:List[MessageDTO] = asyncio.run(
    client.message.pull(fqcn='test.channels.testapp.apps.testorganization.iam.ewc'))
print(messages)
