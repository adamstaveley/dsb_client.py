# swagger_client.ChannelApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channel_controller_create**](ChannelApi.md#channel_controller_create) | **POST** /channel | 

# **channel_controller_create**
> str channel_controller_create(body)



### Example
```python
from __future__ import print_function
import time
import dsb_client.swagger_client
from dsb_client.swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChannelApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateChannelDto() # CreateChannelDto | 

try:
    api_response = api_instance.channel_controller_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelApi->channel_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateChannelDto**](CreateChannelDto.md)|  | 

### Return type

**str**

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

