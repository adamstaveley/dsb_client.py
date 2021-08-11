# LoginReturnDataDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Bearer token used in HTTP \&quot;Authentication\&quot; header to authorize subsequent requests | 
**did** | **str** | DID of messagebroker which is the DID identifier corresponding to env.PRIVATE_KEY | 
**address** | **str** | address of the env.PRIVATE_KEY for signature recovery purposes | 
**signature** | **str** | the compact hex signature which is ECDSA hash(address of privatekey+messagebrokerDID+userDID) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

