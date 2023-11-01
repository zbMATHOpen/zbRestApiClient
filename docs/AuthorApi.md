# swagger_client.AuthorApi

All URIs are relative to *https://api.zbmath.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_author_by_field_author_structured_search_get**](AuthorApi.md#get_author_by_field_author_structured_search_get) | **GET** /author/_structured_search | search authors by descriptive field names
[**get_author_by_syntax_string_author_search_get**](AuthorApi.md#get_author_by_syntax_string_author_search_get) | **GET** /author/_search | search authors by zbMATH style user query
[**get_author_by_zbmath_code_author_code_get**](AuthorApi.md#get_author_by_zbmath_code_author_code_get) | **GET** /author/{code} | get author data by author code
[**intro_author_get**](AuthorApi.md#intro_author_get) | **GET** /author/ | introduction for user help regarding this endpoint

# **get_author_by_field_author_structured_search_get**
> ZbmathApiDataModelsDisplayAuthorsResultSearch get_author_by_field_author_structured_search_get(page=page, results_per_page=results_per_page, author_code=author_code, author_name=author_name, award=award, collectives_of=collectives_of, main_field=main_field, in_collective=in_collective, external_id_type=external_id_type, first_name=first_name, last_name=last_name, reviewer=reviewer, spelling=spelling, state=state)

search authors by descriptive field names

         # Description                    For searching in zbMATH you may employ the Structured Search for         convenient combination of all search fields. While similar to the         1-line syntax search, this endpoint offers much more convenience and         transparency which fields are searched at the cost of search         flexibility.                    # Examples           - **field:** 'author_code', **term:** 'smith.ivan': Search for the         author with the zbMATH code **smith.ivan**.           - **field:** 'author_name', **term:** 'Smith': Search for authors         with the name **Smith**.           - **field:** 'collective', **term:** 'bass.hyman': Search for the         names of the author collective(s) that the author with the zbMATH code         **bass.hyman** is in.           - **field:** 'in_collective', **term:** 'bourbaki.nicolas': Search         for authors that are in the author collective with the zbMATH code         **bourbaki.nicolas**.           # Search fields  - **author_code**: zbMATH code of author - **author_name**: name of author - **award**: awards - **collectives_of**: enter name of collective, result is authors in this collective - **external_id_type**: external Author ID: ORCID, MGP, Wikidata Numbers and others - **first_name**: first Name of the Author - **in_collective**: enter name of author, result is names of collectives the author is in - **last_name**: last Name of the Author - **main_field**: main fields of the Author (given by first two MSC digits) - **reviewer**: reviewer - **spelling**: alternative spellings of the author - **state**: status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthorApi()
page = 0 # int | pagination for result page (optional) (default to 0)
results_per_page = 100 # int |  (optional) (default to 100)
author_code = 'author_code_example' # str | author_code (optional)
author_name = 'author_name_example' # str | author_name (optional)
award = 'award_example' # str | award (optional)
collectives_of = 'collectives_of_example' # str | collectives_of (optional)
main_field = 'main_field_example' # str | main_field (optional)
in_collective = 'in_collective_example' # str | in_collective (optional)
external_id_type = 'external_id_type_example' # str | external_id_type (optional)
first_name = 'first_name_example' # str | first_name (optional)
last_name = 'last_name_example' # str | last_name (optional)
reviewer = 'reviewer_example' # str | reviewer (optional)
spelling = 'spelling_example' # str | spelling (optional)
state = 'state_example' # str | state (optional)

try:
    # search authors by descriptive field names
    api_response = api_instance.get_author_by_field_author_structured_search_get(page=page, results_per_page=results_per_page, author_code=author_code, author_name=author_name, award=award, collectives_of=collectives_of, main_field=main_field, in_collective=in_collective, external_id_type=external_id_type, first_name=first_name, last_name=last_name, reviewer=reviewer, spelling=spelling, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorApi->get_author_by_field_author_structured_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| pagination for result page | [optional] [default to 0]
 **results_per_page** | **int**|  | [optional] [default to 100]
 **author_code** | **str**| author_code | [optional] 
 **author_name** | **str**| author_name | [optional] 
 **award** | **str**| award | [optional] 
 **collectives_of** | **str**| collectives_of | [optional] 
 **main_field** | **str**| main_field | [optional] 
 **in_collective** | **str**| in_collective | [optional] 
 **external_id_type** | **str**| external_id_type | [optional] 
 **first_name** | **str**| first_name | [optional] 
 **last_name** | **str**| last_name | [optional] 
 **reviewer** | **str**| reviewer | [optional] 
 **spelling** | **str**| spelling | [optional] 
 **state** | **str**| state | [optional] 

### Return type

[**ZbmathApiDataModelsDisplayAuthorsResultSearch**](ZbmathApiDataModelsDisplayAuthorsResultSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_author_by_syntax_string_author_search_get**
> ZbmathApiDataModelsDisplayAuthorsResultSearch get_author_by_syntax_string_author_search_get(search_string, page=page, results_per_page=results_per_page)

search authors by zbMATH style user query

         # Description                    The syntax search allows for free logical combinations of all         available search fields. While similar to the structured search,         this endpoint offers much more flexibility at the cost of obscure         search parameters.                    # Examples           - **Simon Donald*** : Search in all parts of an author's name         (results contain Simon, Donald M. and Donaldson, Simon Kirwan).           - **ln:Donald\\* fn:Simon** : Search for specified family and given         name.           - **au:Stefan Müller cc:49** : Combine name search with main MSC         fields           - **au:Helga Bunke** : Search results include name variations,         in particular name changes, different transliterations and         pseudonyms. Names of collectives will be displayed as a separate entity.           - **(st:r & b) | (st:o)** Search results include all reviewers with         biographic information or collectives.           - **(en:MGP | wikidata) ln:a*** : Search results include all         authors having either an entry in the Math Genealogy Project or in         Wikidata and whose family name starts with \"A\".           - **aw:Fields Abel** Search for all Fields Medal Winners who also         received an Abel Prize.            # Search fields  - **ai**: zbMATH code of author - **au**: name of author - **aw**: awards - **cc**: main fields of the Author (given by first two MSC digits) - **cm**: enter name of collective, result is authors in this collective - **co**: enter name of author, result is names of collectives the author is in - **en**: external Author ID: ORCID, MGP, Wikidata Numbers and others - **fn**: first Name of the Author - **ln**: last Name of the Author - **rv**: reviewer - **sp**: alternative spellings of the author - **st**: status            # Operators          - **a & b**: logical and          - **a | b**: logical or          - **!ab**: logical not          - **abc***: right wildcard          - **\"ab c\"**: phrase          - **(ab c)**: parentheses         

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthorApi()
search_string = 'search_string_example' # str | 
page = 0 # int |  (optional) (default to 0)
results_per_page = 100 # int |  (optional) (default to 100)

try:
    # search authors by zbMATH style user query
    api_response = api_instance.get_author_by_syntax_string_author_search_get(search_string, page=page, results_per_page=results_per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorApi->get_author_by_syntax_string_author_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**|  | 
 **page** | **int**|  | [optional] [default to 0]
 **results_per_page** | **int**|  | [optional] [default to 100]

### Return type

[**ZbmathApiDataModelsDisplayAuthorsResultSearch**](ZbmathApiDataModelsDisplayAuthorsResultSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_author_by_zbmath_code_author_code_get**
> ZbmathApiDataModelsDisplayAuthorsResultID get_author_by_zbmath_code_author_code_get(code)

get author data by author code

         # Description                    # About this Endpoint            Use this endpoint if you have the exact zbMATH code of the author in         question. The result will contain only one dataset corresponding to         that code, if entered correctly.            The format of the author's zbMATH code is         **lastname.firstname-additionalname**.            # Example           - **bourbaki.nicolas** is a collective of authors          

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthorApi()
code = 'code_example' # str | 

try:
    # get author data by author code
    api_response = api_instance.get_author_by_zbmath_code_author_code_get(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorApi->get_author_by_zbmath_code_author_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

[**ZbmathApiDataModelsDisplayAuthorsResultID**](ZbmathApiDataModelsDisplayAuthorsResultID.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intro_author_get**
> object intro_author_get()

introduction for user help regarding this endpoint

        # About this Endpoint         For searching in zbMATH you may employ the Structured Search,        which allows for convenient search of all relevant fields.         The syntax search on the other hand allows for free logical        combinations of all available search fields and is much more        flexible. In the following you will find a short explanation of        available search fields.         Use the Authors Search to find information on specific authors.        Author profiles include indexed publications, co-authors,        main fields, and a citation profile.         - **/_search**: make use of the zbMATH search syntax for complex        search. Examples on how to make use of the syntax can be found  in        the endpoint itself.         - **/_structured_search**: a number of fields for a structured        search         - **/{id}**: if a zbMATH id for the author in question is available,        you man enter it here, to return the meta data information of just        this one author.                 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthorApi()

try:
    # introduction for user help regarding this endpoint
    api_response = api_instance.intro_author_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorApi->intro_author_get: %s\n" % e)
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

