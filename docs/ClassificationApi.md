# swagger_client.ClassificationApi

All URIs are relative to *https://api.zbmath.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_classification_by_msc2020_code_classification_code_get**](ClassificationApi.md#get_classification_by_msc2020_code_classification_code_get) | **GET** /classification/{code} | get msc2020 code data by code
[**get_msc2020_by_field_classification_structured_search_get**](ClassificationApi.md#get_msc2020_by_field_classification_structured_search_get) | **GET** /classification/_structured_search | search msc codes meta data by descriptive field names
[**get_msc2020_by_syntax_string_classification_search_get**](ClassificationApi.md#get_msc2020_by_syntax_string_classification_search_get) | **GET** /classification/_search | search msc codes meta data by zbMATH style user query
[**intro_classification_get**](ClassificationApi.md#intro_classification_get) | **GET** /classification/ | introduction for user help regarding this endpoint

# **get_classification_by_msc2020_code_classification_code_get**
> ZbmathApiDataModelsDisplayClassificationsResultID get_classification_by_msc2020_code_classification_code_get(code)

get msc2020 code data by code

         # Description                    # About this Endpoint            Use this endpoint if you have an exact msc2020 classification         code in mind. The result will contain only one dataset         corresponding to that code, if entered correctly.            # Example           - **20J05** leads to information about **\"Homological methods in         group theory\"**         

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClassificationApi()
code = 'code_example' # str | 

try:
    # get msc2020 code data by code
    api_response = api_instance.get_classification_by_msc2020_code_classification_code_get(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationApi->get_classification_by_msc2020_code_classification_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

[**ZbmathApiDataModelsDisplayClassificationsResultID**](ZbmathApiDataModelsDisplayClassificationsResultID.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_msc2020_by_field_classification_structured_search_get**
> ZbmathApiDataModelsDisplayClassificationsResultSearch get_msc2020_by_field_classification_structured_search_get(page=page, results_per_page=results_per_page, code=code, title=title, level=level, parent=parent)

search msc codes meta data by descriptive field names

         # Description                    For searching in zbMATH you may employ the Structured Search for         convenient combination of all search fields. While similar to the         1-line syntax search, this endpoint offers much more convenience and         transparency which fields are searched at the cost of search         flexibility.                    # Examples           - **field:** 'code', **term:** '16E20': Search for the msc code         **16E20**.           - **field:** 'code', **term:** '16': Search for all msc codes         start with **16**.           - **field:** 'title', **term:** 'dynamic': Search for all msc codes         containing the descriptor **dynamic**.          # Search fields  - **code**: msc code (2020) - **level**: level of msc code resolution (0,1,2) - **parent**: parent level of msc code - **title**: descriptive title of msc code

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClassificationApi()
page = 0 # int | result page (optional) (default to 0)
results_per_page = 100 # int |  (optional) (default to 100)
code = 'code_example' # str | code (optional)
title = 'title_example' # str | title (optional)
level = 'level_example' # str | level (optional)
parent = 'parent_example' # str | parent (optional)

try:
    # search msc codes meta data by descriptive field names
    api_response = api_instance.get_msc2020_by_field_classification_structured_search_get(page=page, results_per_page=results_per_page, code=code, title=title, level=level, parent=parent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationApi->get_msc2020_by_field_classification_structured_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| result page | [optional] [default to 0]
 **results_per_page** | **int**|  | [optional] [default to 100]
 **code** | **str**| code | [optional] 
 **title** | **str**| title | [optional] 
 **level** | **str**| level | [optional] 
 **parent** | **str**| parent | [optional] 

### Return type

[**ZbmathApiDataModelsDisplayClassificationsResultSearch**](ZbmathApiDataModelsDisplayClassificationsResultSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_msc2020_by_syntax_string_classification_search_get**
> ZbmathApiDataModelsDisplayClassificationsResultSearch get_msc2020_by_syntax_string_classification_search_get(search_string, page=page, results_per_page=results_per_page)

search msc codes meta data by zbMATH style user query

         # Description                    The syntax search allows for free logical combinations of all         available search fields. While similar to the structured search,         this endpoint offers much more flexibility at the cost of obscure         search parameters.                    # Examples           - **Geometry**: Search for the term Geometry in any field.         Queries are case-independent.          # Search fields  - **cc**: msc code (2020) - **ct**: descriptive title of msc code - **lv**: level of msc code resolution (0,1,2) - **pa**: parent level of msc code            # Operators          - **a & b**: logical and          - **a | b**: logical or          - **!ab**: logical not          - **abc***: right wildcard          - **\"ab c\"**: phrase          - **(ab c)**: parentheses         

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClassificationApi()
search_string = 'search_string_example' # str | 
page = 0 # int |  (optional) (default to 0)
results_per_page = 100 # int |  (optional) (default to 100)

try:
    # search msc codes meta data by zbMATH style user query
    api_response = api_instance.get_msc2020_by_syntax_string_classification_search_get(search_string, page=page, results_per_page=results_per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationApi->get_msc2020_by_syntax_string_classification_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**|  | 
 **page** | **int**|  | [optional] [default to 0]
 **results_per_page** | **int**|  | [optional] [default to 100]

### Return type

[**ZbmathApiDataModelsDisplayClassificationsResultSearch**](ZbmathApiDataModelsDisplayClassificationsResultSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intro_classification_get**
> object intro_classification_get()

introduction for user help regarding this endpoint

        # About this Endpoint         For searching in zbMATH you may employ the Structured Search,        which allows for convenient search of all relevant fields.         The syntax search on the other hand allows for free logical        combinations of all available search fields and is much more        flexible. In the following you will find a short explanation of        available search fields.         Use the Classification Search to find information on msc codes of        research fields of interest. msc2020 codes available only.                  **Level 0:** first two digits of msc code         **Level 1:** first two digits plus letter of msc code         **Level 2:** full msc code                           - **/_search**: make use of the zbmath search syntax for complex         search. Examples on how to make use of the syntax can be found in         the endpoint itself.         - **/_structured_search**: a number of fields for a structured search         - **/{msc_code}**: if an identifier for the msc2020 code in        question is available, you man enter it here, to return the meta data        information of just this one msc2020 code.          

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClassificationApi()

try:
    # introduction for user help regarding this endpoint
    api_response = api_instance.intro_classification_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationApi->intro_classification_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

