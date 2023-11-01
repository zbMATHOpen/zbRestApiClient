# swagger_client.SoftwareApi

All URIs are relative to *https://api.zbmath.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_software_by_field_software_structured_search_get**](SoftwareApi.md#get_software_by_field_software_structured_search_get) | **GET** /software/_structured_search | search software meta data by descriptive field names
[**get_software_by_id_software_id_get**](SoftwareApi.md#get_software_by_id_software_id_get) | **GET** /software/{id} | get software data by software id
[**get_software_by_syntax_string_software_search_get**](SoftwareApi.md#get_software_by_syntax_string_software_search_get) | **GET** /software/_search | search software meta data by zbMATH style user query
[**intro_software_get**](SoftwareApi.md#intro_software_get) | **GET** /software/ | introduction for user help regarding this endpoint software

# **get_software_by_field_software_structured_search_get**
> ZbmathApiDataModelsDisplaySoftwareResultSearch get_software_by_field_software_structured_search_get(page=page, results_per_page=results_per_page, author=author, description=description, keyword=keyword, msc=msc, name=name, programming_language=programming_language)

search software meta data by descriptive field names

         # Description                    For searching in zbMATH you may employ the Structured Search for         convenient combination of all search fields. While similar to the         1-line syntax search, this endpoint offers much more convenience and         transparency which fields are searched at the cost of search         flexibility.                    # Examples           - **field:** 'author', **term:** 'smith': Search for author named         **Smith**           - **field:** 'keyword', **term:** 'dynamic': Search for keyword         **dynamic** associated with the software           - **field:** 'programming_language', **term:** 'python': Search for         software based on the programming language **python**.          # Search fields  - **author**: name of author - **description**: description text - **keyword**: keyword - **msc**: related msc code - **name**: name of software - **programming_language**: programming language

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareApi()
page = 0 # int |  (optional) (default to 0)
results_per_page = 100 # int |  (optional) (default to 100)
author = 'author_example' # str | author (optional)
description = 'description_example' # str | description (optional)
keyword = 'keyword_example' # str | keyword (optional)
msc = 'msc_example' # str | msc (optional)
name = 'name_example' # str | name (optional)
programming_language = 'programming_language_example' # str | programming_language (optional)

try:
    # search software meta data by descriptive field names
    api_response = api_instance.get_software_by_field_software_structured_search_get(page=page, results_per_page=results_per_page, author=author, description=description, keyword=keyword, msc=msc, name=name, programming_language=programming_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->get_software_by_field_software_structured_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **results_per_page** | **int**|  | [optional] [default to 100]
 **author** | **str**| author | [optional] 
 **description** | **str**| description | [optional] 
 **keyword** | **str**| keyword | [optional] 
 **msc** | **str**| msc | [optional] 
 **name** | **str**| name | [optional] 
 **programming_language** | **str**| programming_language | [optional] 

### Return type

[**ZbmathApiDataModelsDisplaySoftwareResultSearch**](ZbmathApiDataModelsDisplaySoftwareResultSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_software_by_id_software_id_get**
> ZbmathApiDataModelsDisplaySoftwareResultID get_software_by_id_software_id_get(id)

get software data by software id

         # Description                    # About this Endpoint            Use this endpoint if you have the exact zbMATH id of the software in         question. The result will contain only one dataset corresponding to         that id, if entered correctly.            # Example           - **12**         

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareApi()
id = 'id_example' # str | 

try:
    # get software data by software id
    api_response = api_instance.get_software_by_id_software_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->get_software_by_id_software_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ZbmathApiDataModelsDisplaySoftwareResultID**](ZbmathApiDataModelsDisplaySoftwareResultID.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_software_by_syntax_string_software_search_get**
> ZbmathApiDataModelsDisplaySoftwareResultSearch get_software_by_syntax_string_software_search_get(search_string, page=page, results_per_page=results_per_page)

search software meta data by zbMATH style user query

         # Description                    The syntax search allows for free logical combinations of all         available search fields. While similar to the structured search,         this endpoint offers much more flexibility at the cost of obscure         search parameters.                    # Examples           - **sw:Sage***: Search for a specific software package.           - **ab:geometry & ut:ORMS**: Search for software packages with the         word \"geometry\" in the description, and which have the keyword ORMS (         Oberwolfach Registry of Mathematical Software). The operator \"&\" is the         default and may be omitted.           - **cc:13 | 14**: Search for software packages which are cited by         articles belonging to the MSC sections 13 and 14.           - **GAP au:Eick**: Search for a term in the \"any\" index (which also         includes dependencies) and by software author.           - **pl:Java & ab:R**: Search for software package programmed in         Java whose description text contains \"R\"          # Search fields  - **ab**: description text - **au**: name of author - **cc**: related msc code - **pl**: programming language - **sw**: name of software - **ut**: keyword            # Operators          - **a & b**: logical and          - **a | b**: logical or          - **!ab**: logical not          - **abc***: right wildcard          - **\"ab c\"**: phrase          - **(ab c)**: parentheses         

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareApi()
search_string = 'search_string_example' # str | 
page = 0 # int |  (optional) (default to 0)
results_per_page = 100 # int |  (optional) (default to 100)

try:
    # search software meta data by zbMATH style user query
    api_response = api_instance.get_software_by_syntax_string_software_search_get(search_string, page=page, results_per_page=results_per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->get_software_by_syntax_string_software_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**|  | 
 **page** | **int**|  | [optional] [default to 0]
 **results_per_page** | **int**|  | [optional] [default to 100]

### Return type

[**ZbmathApiDataModelsDisplaySoftwareResultSearch**](ZbmathApiDataModelsDisplaySoftwareResultSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intro_software_get**
> object intro_software_get()

introduction for user help regarding this endpoint software

        # About this Endpoint         For searching in zbMATH you may employ the Structured Search,        which allows for convenient search of all relevant fields.         The syntax search on the other hand allows for free logical        combinations of all available search fields and is much more        flexible. In the following you will find a short explanation of        available search fields.         Use the Software Search to find information on specific software        and where it is used.                  - **/_search**: make use of the zbMATH search syntax for complex        search. Examples on how to make use of the syntax can be found in        the endpoint itself.         - **/_structured_search**: a number of fields for a structured search         - **/{id}**: if a zbMATH id for the software in question is        available, you man enter it here, to return the meta data information        of just this one software entry.        

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareApi()

try:
    # introduction for user help regarding this endpoint software
    api_response = api_instance.intro_software_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->intro_software_get: %s\n" % e)
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

