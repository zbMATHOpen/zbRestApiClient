# swagger_client.DocumentApi

All URIs are relative to *https://api.zbmath.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_document_by_field_document_structured_search_get**](DocumentApi.md#get_document_by_field_document_structured_search_get) | **GET** /document/_structured_search | search documents by descriptive field names
[**get_document_by_syntax_string_document_search_get**](DocumentApi.md#get_document_by_syntax_string_document_search_get) | **GET** /document/_search | search documents by zbMATH style user query
[**get_document_by_zbmath_id_document_id_get**](DocumentApi.md#get_document_by_zbmath_id_document_id_get) | **GET** /document/{id} | get document data by zbMath ID
[**intro_document_get**](DocumentApi.md#intro_document_get) | **GET** /document/ | introduction for user help regarding this endpoint

# **get_document_by_field_document_structured_search_get**
> ZbmathApiDataModelsDisplayDocumentsResultSearch get_document_by_field_document_structured_search_get(page=page, results_per_page=results_per_page, review_text=review_text, unique_contributor_code=unique_contributor_code, contributor_code=contributor_code, zbmath_id=zbmath_id, author_reference_code=author_reference_code, contributor_name=contributor_name, biographic_reference_code=biographic_reference_code, biographic_reference_name=biographic_reference_name, unique_author_code=unique_author_code, msc_title=msc_title, msc_code=msc_code, citing=citing, database=database, document_type=document_type, unique_editor_code=unique_editor_code, editor_name=editor_name, editor_code=editor_code, external_id__type=external_id__type, author_code=author_code, issue_id=issue_id, language=language, related_url=related_url, author_count=author_count, reviewing_state=reviewing_state, publisher=publisher, year=year, reference_author_code=reference_author_code, reference_msc=reference_msc, reference_zbmath_id=reference_zbmath_id, reference_text=reference_text, reference_series_id=reference_series_id, reviewer_code=reviewer_code, reviewer_name=reviewer_name, reference_year=reference_year, series_id=series_id, software_id=software_id, source=source, state=state, software_name=software_name, title=title, keyword=keyword)

search documents by descriptive field names

         # Description                    For searching in zbMATH you may employ the Structured Search for         convenient combination of all search fields. While similar to the         1-line syntax search, this endpoint offers much more convenience and         transparency which fields are searched at the cost of search         flexibility.                    # Examples           - **field:** 'contributor_name', **term:** 'smith': Search for         author, author reference or editor named **Smith**           - **field:** 'year', **term:** '2002-2005': Search for documents         published in the years from **2002* until **2005**           - **field:** 'reference_author_code', **term:** 'smith.ivan':         Search for documents with references that were written by the author         with the zbMATH code **smith.ivan**           - **field:** 'reference_zbmath_id', **term:** '6383667': Search for         documents that reference to a document with the zbMATH id **6383667**           - **field:** 'zbmath_id', **term:** '6383667': Search for the         document with the zbMATH id **6383667**. zbMATH id includes all types         of identifiers used on zbmath.org, i.e.: pre ID, Zbl ID, JFM ID,         ERAM ID          # Search fields  - **author_code**: zbMATH author code - **author_count**: number of authors of the document in question - **author_reference_code**: zbMATH code of an author reference - **biographic_reference_code**: zbMATH code of the biographic reference - **biographic_reference_name**: name of the biographic reference - **citing**: cited documents - **contributor_code**: zbMATH code of any contributor of a document - **contributor_name**: name of any contributor of a document - **database**: database name - **document_type**: type of a document - **editor_code**: zbMATH code of editor - **editor_name**: name of editor - **external_id / type**: external identifier or type - **issue_id**: zbMATH id of the corresponding issue - **keyword**: keyword of the document - **language**: language - **msc_code**: msc code (any level) - **msc_title**: title of msc code - **publisher**: publisher - **reference_author_code**: zbMATH code of author in reference - **reference_msc**: msc code of reference - **reference_series_id**: zbMATH id of serial - **reference_text**: reference text - **reference_year**: publishing year of reference - **reference_zbmath_id**: zbMATH id of reference - **related url**: related url - **review_text**: review text - **reviewer_code**: zbMATH code of reviewer - **reviewer_name**: name of reviewer - **reviewing_state**: reviewing state - **series_id**: zbMATH id of serial - **software_id**: zbMATH id of related software - **software_name**: name of related software - **source**: name of source - **state**: state of publication - **title**: title - **unique_author_code**: zbMATH code of a uniquely identified author of a document - **unique_contributor_code**: zbMATH code of a uniquely identified contributor of a document - **unique_editor_code**: zbMATH code of a uniquely identified editor of a document - **year**: year of publishing (range of year possible: XXXX-YYYY) - **zbmath_id**: zbMATH id of document. This includes all types of identifiers used on zbmath.org, i.e.: pre ID, Zbl ID, JFM ID, ERAM ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DocumentApi()
page = 0 # int | pagination for result page (optional) (default to 0)
results_per_page = 100 # int |  (optional) (default to 100)
review_text = 'review_text_example' # str | review_text (optional)
unique_contributor_code = 'unique_contributor_code_example' # str | unique_contributor_code (optional)
contributor_code = 'contributor_code_example' # str | contributor_code (optional)
zbmath_id = 'zbmath_id_example' # str | zbmath_id (optional)
author_reference_code = 'author_reference_code_example' # str | author_reference_code (optional)
contributor_name = 'contributor_name_example' # str | contributor_name (optional)
biographic_reference_code = 'biographic_reference_code_example' # str | biographic_reference_code (optional)
biographic_reference_name = 'biographic_reference_name_example' # str | biographic_reference_name (optional)
unique_author_code = 'unique_author_code_example' # str | unique_author_code (optional)
msc_title = 'msc_title_example' # str | msc_title (optional)
msc_code = 'msc_code_example' # str | msc_code (optional)
citing = 'citing_example' # str | citing (optional)
database = 'database_example' # str | database (optional)
document_type = 'document_type_example' # str | document_type (optional)
unique_editor_code = 'unique_editor_code_example' # str | unique_editor_code (optional)
editor_name = 'editor_name_example' # str | editor_name (optional)
editor_code = 'editor_code_example' # str | editor_code (optional)
external_id__type = 'external_id__type_example' # str | external_id / type (optional)
author_code = 'author_code_example' # str | author_code (optional)
issue_id = 'issue_id_example' # str | issue_id (optional)
language = 'language_example' # str | language (optional)
related_url = 'related_url_example' # str | related url (optional)
author_count = 'author_count_example' # str | author_count (optional)
reviewing_state = 'reviewing_state_example' # str | reviewing_state (optional)
publisher = 'publisher_example' # str | publisher (optional)
year = 'year_example' # str | year (optional)
reference_author_code = 'reference_author_code_example' # str | reference_author_code (optional)
reference_msc = 'reference_msc_example' # str | reference_msc (optional)
reference_zbmath_id = 'reference_zbmath_id_example' # str | reference_zbmath_id (optional)
reference_text = 'reference_text_example' # str | reference_text (optional)
reference_series_id = 'reference_series_id_example' # str | reference_series_id (optional)
reviewer_code = 'reviewer_code_example' # str | reviewer_code (optional)
reviewer_name = 'reviewer_name_example' # str | reviewer_name (optional)
reference_year = 'reference_year_example' # str | reference_year (optional)
series_id = 'series_id_example' # str | series_id (optional)
software_id = 'software_id_example' # str | software_id (optional)
source = 'source_example' # str | source (optional)
state = 'state_example' # str | state (optional)
software_name = 'software_name_example' # str | software_name (optional)
title = 'title_example' # str | title (optional)
keyword = 'keyword_example' # str | keyword (optional)

try:
    # search documents by descriptive field names
    api_response = api_instance.get_document_by_field_document_structured_search_get(page=page, results_per_page=results_per_page, review_text=review_text, unique_contributor_code=unique_contributor_code, contributor_code=contributor_code, zbmath_id=zbmath_id, author_reference_code=author_reference_code, contributor_name=contributor_name, biographic_reference_code=biographic_reference_code, biographic_reference_name=biographic_reference_name, unique_author_code=unique_author_code, msc_title=msc_title, msc_code=msc_code, citing=citing, database=database, document_type=document_type, unique_editor_code=unique_editor_code, editor_name=editor_name, editor_code=editor_code, external_id__type=external_id__type, author_code=author_code, issue_id=issue_id, language=language, related_url=related_url, author_count=author_count, reviewing_state=reviewing_state, publisher=publisher, year=year, reference_author_code=reference_author_code, reference_msc=reference_msc, reference_zbmath_id=reference_zbmath_id, reference_text=reference_text, reference_series_id=reference_series_id, reviewer_code=reviewer_code, reviewer_name=reviewer_name, reference_year=reference_year, series_id=series_id, software_id=software_id, source=source, state=state, software_name=software_name, title=title, keyword=keyword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->get_document_by_field_document_structured_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| pagination for result page | [optional] [default to 0]
 **results_per_page** | **int**|  | [optional] [default to 100]
 **review_text** | **str**| review_text | [optional] 
 **unique_contributor_code** | **str**| unique_contributor_code | [optional] 
 **contributor_code** | **str**| contributor_code | [optional] 
 **zbmath_id** | **str**| zbmath_id | [optional] 
 **author_reference_code** | **str**| author_reference_code | [optional] 
 **contributor_name** | **str**| contributor_name | [optional] 
 **biographic_reference_code** | **str**| biographic_reference_code | [optional] 
 **biographic_reference_name** | **str**| biographic_reference_name | [optional] 
 **unique_author_code** | **str**| unique_author_code | [optional] 
 **msc_title** | **str**| msc_title | [optional] 
 **msc_code** | **str**| msc_code | [optional] 
 **citing** | **str**| citing | [optional] 
 **database** | **str**| database | [optional] 
 **document_type** | **str**| document_type | [optional] 
 **unique_editor_code** | **str**| unique_editor_code | [optional] 
 **editor_name** | **str**| editor_name | [optional] 
 **editor_code** | **str**| editor_code | [optional] 
 **external_id__type** | **str**| external_id / type | [optional] 
 **author_code** | **str**| author_code | [optional] 
 **issue_id** | **str**| issue_id | [optional] 
 **language** | **str**| language | [optional] 
 **related_url** | **str**| related url | [optional] 
 **author_count** | **str**| author_count | [optional] 
 **reviewing_state** | **str**| reviewing_state | [optional] 
 **publisher** | **str**| publisher | [optional] 
 **year** | **str**| year | [optional] 
 **reference_author_code** | **str**| reference_author_code | [optional] 
 **reference_msc** | **str**| reference_msc | [optional] 
 **reference_zbmath_id** | **str**| reference_zbmath_id | [optional] 
 **reference_text** | **str**| reference_text | [optional] 
 **reference_series_id** | **str**| reference_series_id | [optional] 
 **reviewer_code** | **str**| reviewer_code | [optional] 
 **reviewer_name** | **str**| reviewer_name | [optional] 
 **reference_year** | **str**| reference_year | [optional] 
 **series_id** | **str**| series_id | [optional] 
 **software_id** | **str**| software_id | [optional] 
 **source** | **str**| source | [optional] 
 **state** | **str**| state | [optional] 
 **software_name** | **str**| software_name | [optional] 
 **title** | **str**| title | [optional] 
 **keyword** | **str**| keyword | [optional] 

### Return type

[**ZbmathApiDataModelsDisplayDocumentsResultSearch**](ZbmathApiDataModelsDisplayDocumentsResultSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_by_syntax_string_document_search_get**
> ZbmathApiDataModelsDisplayDocumentsResultSearch get_document_by_syntax_string_document_search_get(search_string, page=page, results_per_page=results_per_page)

search documents by zbMATH style user query

         # Description                    The syntax search allows for free logical combinations of all         available search fields. While similar to the structured search,         this endpoint offers much more flexibility at the cost of obscure         search parameters.                    # Examples           - **Geometry**: Search for the term Geometry in any field. Queries are         case-independent.           - **Funct***: Wildcard queries are specified by * (e.g. functions,         functorial, etc.). Otherwise the search is exact.           - **\"Topological group\"**: Phrases (multi-words) should be set in         \"straight quotation marks\".           - **au: Bourbaki & ti: Algebra**: Search for author and title. The         and-operator & is default and can be omitted.           - **Chebyshev | Tschebyscheff**: The or-operator | allows to         search for Chebyshev or Tschebyscheff.           - **Quasi\\* map\\* py: 1989**: The resulting documents have         publication         year 1989.           - **so: Eur\\* J\\* Mat\\* Soc\\* cc: 14**: Search for publications in a         particular source with a Mathematics Subject Classification code (cc)         in 14.           - **\"Partial diff\\* eq\\*\" ! elliptic**: The not-operator ! eliminates         all results containing the word elliptic.           - **dt: b & au: Hilbert**: The document type is set to books;         alternatively: j for journal articles, a for book articles.           - **py: 2000-2015 cc: (94A | 11T)**: Number ranges are accepted.         Terms can be grouped within (parentheses).           - **la: chinese**: Find documents in a given language. ISO 639-1         (opens in new tab) language codes can also be used.          # Search fields  - **ab**: review text - **ac**: zbMATH code of a uniquely identified contributor of a document - **ai**: zbMATH code of any contributor of a document - **an**: zbMATH id of document. This includes all types of identifiers used on zbmath.org, i.e.: pre ID, Zbl ID, JFM ID, ERAM ID - **ar**: zbMATH code of an author reference - **au**: name of any contributor of a document - **bi**: zbMATH code of the biographic reference - **br**: name of the biographic reference - **ca**: zbMATH code of a uniquely identified author of a document - **cc**: title of msc code - **cca**: msc code (any level) - **ci**: cited documents - **db**: database name - **dt**: type of a document - **ec**: zbMATH code of a uniquely identified editor of a document - **ed**: name of editor - **ei**: zbMATH code of editor - **en**: external identifier or type - **ia**: zbMATH author code - **in**: zbMATH id of the corresponding issue - **la**: language - **li**: related url - **na**: number of authors of the document in question - **pt**: reviewing state - **pu**: publisher - **py**: year of publishing (range of year possible: XXXX-YYYY) - **ra**: zbMATH code of author in reference - **rc**: msc code of reference - **rf**: zbMATH id of reference - **rft**: reference text - **rj**: zbMATH id of serial - **rn**: zbMATH code of reviewer - **rv**: name of reviewer - **ry**: publishing year of reference - **se**: zbMATH id of serial - **si**: zbMATH id of related software - **so**: name of source - **st**: state of publication - **sw**: name of related software - **ti**: title - **ut**: keyword of the document            # Operators          - **a & b**: logical and          - **a | b**: logical or          - **!ab**: logical not          - **abc***: right wildcard          - **\"ab c\"**: phrase          - **(ab c)**: parentheses         

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DocumentApi()
search_string = 'search_string_example' # str | 
page = 0 # int |  (optional) (default to 0)
results_per_page = 100 # int |  (optional) (default to 100)

try:
    # search documents by zbMATH style user query
    api_response = api_instance.get_document_by_syntax_string_document_search_get(search_string, page=page, results_per_page=results_per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->get_document_by_syntax_string_document_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**|  | 
 **page** | **int**|  | [optional] [default to 0]
 **results_per_page** | **int**|  | [optional] [default to 100]

### Return type

[**ZbmathApiDataModelsDisplayDocumentsResultSearch**](ZbmathApiDataModelsDisplayDocumentsResultSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_by_zbmath_id_document_id_get**
> ZbmathApiDataModelsDisplayDocumentsResultID get_document_by_zbmath_id_document_id_get(id)

get document data by zbMath ID

         # Description                    # About this Endpoint            Use this endpoint if you have an zbMATH id of the document in         question. The result will contain only one dataset corresponding to         that id, if entered correctly.            # Example           - **6383667**         

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DocumentApi()
id = 'id_example' # str | 

try:
    # get document data by zbMath ID
    api_response = api_instance.get_document_by_zbmath_id_document_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->get_document_by_zbmath_id_document_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ZbmathApiDataModelsDisplayDocumentsResultID**](ZbmathApiDataModelsDisplayDocumentsResultID.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intro_document_get**
> object intro_document_get()

introduction for user help regarding this endpoint

        # About this Endpoint         For searching in zbMATH you may employ the Structured Search,        which allows for convenient search of all relevant fields.         The syntax search on the other hand allows for free logical        combinations of all available search fields and is much more        flexible. In the following you will find a short explanation of        available search fields.         Use the Documents Search to find documents on specific topics,        by title or other characteristics. To find all publications by a        specific author or from a specific journal you should instead use the        respective search tab.                  - **/_search**: make use of the zbmath search syntax for complex        search. Examples on how to make use of the syntax can be found in        the endpoint itself.         - **/_structured_search**: a number of fields for a structured search         - **/{id}**: if a zbMATH id for the document in question is        available, you man enter it here, to return the meta data information        of just this one author.        

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DocumentApi()

try:
    # introduction for user help regarding this endpoint
    api_response = api_instance.intro_document_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->intro_document_get: %s\n" % e)
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

