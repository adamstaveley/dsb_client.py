# swagger_client.AuthApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_controller_login**](AuthApi.md#auth_controller_login) | **POST** /auth/login | 

# **auth_controller_login**
> LoginReturnDataDTO auth_controller_login(body)



### Example
```python
from __future__ import print_function
import time
import dsb_client.swagger_client
from dsb_client.swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
body = swagger_client.LoginDataDTO() # LoginDataDTO | 

try:
    api_response = api_instance.auth_controller_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_controller_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginDataDTO**](LoginDataDTO.md)|  | 

### Return type

[**LoginReturnDataDTO**](LoginReturnDataDTO.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

