# swagger_client.SerialApi

All URIs are relative to *https://api.zbmath.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_serial_by_field_serial_structured_search_get**](SerialApi.md#get_serial_by_field_serial_structured_search_get) | **GET** /serial/_structured_search | search serial meta data by descriptive field names
[**get_serial_by_id_serial_id_get**](SerialApi.md#get_serial_by_id_serial_id_get) | **GET** /serial/{id} | get serial data by serial id
[**get_serial_by_syntax_string_serial_search_get**](SerialApi.md#get_serial_by_syntax_string_serial_search_get) | **GET** /serial/_search | search serial meta data by zbMATH style user query
[**intro_serial_get**](SerialApi.md#intro_serial_get) | **GET** /serial/ | introduction for user help regarding this endpoint serial

# **get_serial_by_field_serial_structured_search_get**
> ZbmathApiDataModelsDisplaySerialsResultSearch get_serial_by_field_serial_structured_search_get(page=page, results_per_page=results_per_page, country=country, issn=issn, language=language, main_field=main_field, publisher=publisher, state=state, serial_type=serial_type, title=title, url=url, year=year)

search serial meta data by descriptive field names

         # Description                    For searching in zbMATH you may employ the Structured Search for         convenient combination of all search fields. While similar to the         1-line syntax search, this endpoint offers much more convenience and         transparency which fields are searched at the cost of search         flexibility.                    # Examples           - field: 'title', term: 'Annals of Mathematics': Search for         journal title phrase.           - field: 'year', term: '1800-1899': Search for 19th century serials          # Search fields  - **country**: country - **issn**: issn - **language**: language - **main_field**: main fields - **publisher**: publisher - **serial_type**: serial_type - **state**: state - **title**: title - **url**: related url - **year**: year of publishing (range of year possible: XXXX-YYYY)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SerialApi()
page = 0 # int | pagination for result page (optional) (default to 0)
results_per_page = 100 # int |  (optional) (default to 100)
country = 'country_example' # str | country (optional)
issn = 'issn_example' # str | issn (optional)
language = 'language_example' # str | language (optional)
main_field = 'main_field_example' # str | main_field (optional)
publisher = 'publisher_example' # str | publisher (optional)
state = 'state_example' # str | state (optional)
serial_type = 'serial_type_example' # str | serial_type (optional)
title = 'title_example' # str | title (optional)
url = 'url_example' # str | url (optional)
year = 'year_example' # str | year (optional)

try:
    # search serial meta data by descriptive field names
    api_response = api_instance.get_serial_by_field_serial_structured_search_get(page=page, results_per_page=results_per_page, country=country, issn=issn, language=language, main_field=main_field, publisher=publisher, state=state, serial_type=serial_type, title=title, url=url, year=year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SerialApi->get_serial_by_field_serial_structured_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| pagination for result page | [optional] [default to 0]
 **results_per_page** | **int**|  | [optional] [default to 100]
 **country** | **str**| country | [optional] 
 **issn** | **str**| issn | [optional] 
 **language** | **str**| language | [optional] 
 **main_field** | **str**| main_field | [optional] 
 **publisher** | **str**| publisher | [optional] 
 **state** | **str**| state | [optional] 
 **serial_type** | **str**| serial_type | [optional] 
 **title** | **str**| title | [optional] 
 **url** | **str**| url | [optional] 
 **year** | **str**| year | [optional] 

### Return type

[**ZbmathApiDataModelsDisplaySerialsResultSearch**](ZbmathApiDataModelsDisplaySerialsResultSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_serial_by_id_serial_id_get**
> ZbmathApiDataModelsDisplaySerialsResultID get_serial_by_id_serial_id_get(id)

get serial data by serial id

         # Description                    # About this Endpoint            Use this endpoint if you have the exact zbMATH id of the serial in         question. The result will contain only one dataset corresponding to         that id, if entered correctly.            # Example           - **3191**: leads to information about serial **\"Advances in         Difference Equations\"**         

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SerialApi()
id = 'id_example' # str | 

try:
    # get serial data by serial id
    api_response = api_instance.get_serial_by_id_serial_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SerialApi->get_serial_by_id_serial_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ZbmathApiDataModelsDisplaySerialsResultID**](ZbmathApiDataModelsDisplaySerialsResultID.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_serial_by_syntax_string_serial_search_get**
> ZbmathApiDataModelsDisplaySerialsResultSearch get_serial_by_syntax_string_serial_search_get(search_string, page=page, results_per_page=results_per_page)

search serial meta data by zbMATH style user query

         # Description                    The syntax search allows for free logical combinations of all         available search fields. While similar to the structured search,         this endpoint offers much more flexibility at the cost of obscure         search parameters.                    # Examples           - **Ann\\* Math***: Search for the expressions in all fields.         Abbreviations are also possible.           - **jt:\"Annals of Mathematics\"**: Search for journal title phrase.           - **jt:annals pu:mathematics**: Search for title and publisher.           - **sn:0003-486X**: Search for ISSN. Both electronic and print ISSN         are accepted.           - **se:00002531**: Search for the exact serial identifier. This         excludes homonyms. Compare to jt:Annals of Mathematics.           - **jt:Annals cc:05**: Search for title and main field.           - **jt:Annals (cy:cn | ro)**: Search for title and country.           - **tp:j st:o v t**: Search for journals which are open access and         currently indexed cover-to-cover.           - **py:1800-1899 la:no**: Search for 19th century serials which         published in Norwegian.          # Search fields  - **cc**: main fields - **cy**: country - **jt**: title - **la**: language - **li**: related url - **pu**: publisher - **py**: year of publishing (range of year possible: XXXX-YYYY) - **sn**: issn - **st**: state - **tp**: serial_type            # Operators          - **a & b**: logical and          - **a | b**: logical or          - **!ab**: logical not          - **abc***: right wildcard          - **\"ab c\"**: phrase          - **(ab c)**: parentheses         

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SerialApi()
search_string = 'search_string_example' # str | 
page = 0 # int |  (optional) (default to 0)
results_per_page = 100 # int |  (optional) (default to 100)

try:
    # search serial meta data by zbMATH style user query
    api_response = api_instance.get_serial_by_syntax_string_serial_search_get(search_string, page=page, results_per_page=results_per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SerialApi->get_serial_by_syntax_string_serial_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**|  | 
 **page** | **int**|  | [optional] [default to 0]
 **results_per_page** | **int**|  | [optional] [default to 100]

### Return type

[**ZbmathApiDataModelsDisplaySerialsResultSearch**](ZbmathApiDataModelsDisplaySerialsResultSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intro_serial_get**
> object intro_serial_get()

introduction for user help regarding this endpoint serial

          # About this Endpoint           For searching in zbMATH you may employ the Structured Search,         which allows for convenient search of all relevant fields.           The syntax search on the other hand allows for free logical         combinations of all available search fields and is much more         flexible. In the following you will find a short explanation of         available search fields.           Use the Serials Search to find information on journals or book         serial. Serial profiles include indexed publications, volume lists,         frequent authors and subjects, open access status, and citation profile.                    - **/_search**: make use of the zbMATH search syntax for complex         search. Examples on how to make use of the syntax can be found in         the endpoint itself.          - **/_structured_search**: a number of fields for a structured search          - **/{id}**: if a zbMATH id for the software in question is         available, you man enter it here, to return the meta data         information of just this one serial entry.          

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SerialApi()

try:
    # introduction for user help regarding this endpoint serial
    api_response = api_instance.intro_serial_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SerialApi->intro_serial_get: %s\n" % e)
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

