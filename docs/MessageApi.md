# swagger_client.MessageApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**message_controller_get_new_from_channel**](MessageApi.md#message_controller_get_new_from_channel) | **GET** /message | 
[**message_controller_publish**](MessageApi.md#message_controller_publish) | **POST** /message | 

# **message_controller_get_new_from_channel**
> list[MessageDTO] message_controller_get_new_from_channel(fqcn, amount=amount)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MessageApi(swagger_client.ApiClient(configuration))
fqcn = 'fqcn_example' # str | Fully qualified channel name (fqcn)
amount = 'amount_example' # str | Amount of messages to be returned in the request, default value is 100 (optional)

try:
    api_response = api_instance.message_controller_get_new_from_channel(fqcn, amount=amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_controller_get_new_from_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqcn** | **str**| Fully qualified channel name (fqcn) | 
 **amount** | **str**| Amount of messages to be returned in the request, default value is 100 | [optional] 

### Return type

[**list[MessageDTO]**](MessageDTO.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_controller_publish**
> str message_controller_publish(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MessageApi(swagger_client.ApiClient(configuration))
body = swagger_client.PublishMessageDto() # PublishMessageDto | 

try:
    api_response = api_instance.message_controller_publish(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_controller_publish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PublishMessageDto**](PublishMessageDto.md)|  | 

### Return type

**str**

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

