# swagger_client.HealthApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_controller_check**](HealthApi.md#health_controller_check) | **GET** /health | 

# **health_controller_check**
> InlineResponse200 health_controller_check()



### Example
```python
from __future__ import print_function
import time
import dsb_client.swagger_client
from dsb_client.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HealthApi()

try:
    api_response = api_instance.health_controller_check()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->health_controller_check: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

