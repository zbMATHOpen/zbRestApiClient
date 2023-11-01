# swagger-client
a REST api for zbMATH Open, currently with endpoints for authors, classifications, documents, serials and software

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v0.4.3rc0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthorApi(swagger_client.ApiClient(configuration))
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

# create an instance of the API class
api_instance = swagger_client.AuthorApi(swagger_client.ApiClient(configuration))
search_string = 'search_string_example' # str | 
page = 0 # int |  (optional) (default to 0)
results_per_page = 100 # int |  (optional) (default to 100)

try:
    # search authors by zbMATH style user query
    api_response = api_instance.get_author_by_syntax_string_author_search_get(search_string, page=page, results_per_page=results_per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorApi->get_author_by_syntax_string_author_search_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AuthorApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | 

try:
    # get author data by author code
    api_response = api_instance.get_author_by_zbmath_code_author_code_get(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorApi->get_author_by_zbmath_code_author_code_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AuthorApi(swagger_client.ApiClient(configuration))

try:
    # introduction for user help regarding this endpoint
    api_response = api_instance.intro_author_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorApi->intro_author_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.zbmath.org*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthorApi* | [**get_author_by_field_author_structured_search_get**](docs/AuthorApi.md#get_author_by_field_author_structured_search_get) | **GET** /author/_structured_search | search authors by descriptive field names
*AuthorApi* | [**get_author_by_syntax_string_author_search_get**](docs/AuthorApi.md#get_author_by_syntax_string_author_search_get) | **GET** /author/_search | search authors by zbMATH style user query
*AuthorApi* | [**get_author_by_zbmath_code_author_code_get**](docs/AuthorApi.md#get_author_by_zbmath_code_author_code_get) | **GET** /author/{code} | get author data by author code
*AuthorApi* | [**intro_author_get**](docs/AuthorApi.md#intro_author_get) | **GET** /author/ | introduction for user help regarding this endpoint
*ClassificationApi* | [**get_classification_by_msc2020_code_classification_code_get**](docs/ClassificationApi.md#get_classification_by_msc2020_code_classification_code_get) | **GET** /classification/{code} | get msc2020 code data by code
*ClassificationApi* | [**get_msc2020_by_field_classification_structured_search_get**](docs/ClassificationApi.md#get_msc2020_by_field_classification_structured_search_get) | **GET** /classification/_structured_search | search msc codes meta data by descriptive field names
*ClassificationApi* | [**get_msc2020_by_syntax_string_classification_search_get**](docs/ClassificationApi.md#get_msc2020_by_syntax_string_classification_search_get) | **GET** /classification/_search | search msc codes meta data by zbMATH style user query
*ClassificationApi* | [**intro_classification_get**](docs/ClassificationApi.md#intro_classification_get) | **GET** /classification/ | introduction for user help regarding this endpoint
*DocumentApi* | [**get_document_by_field_document_structured_search_get**](docs/DocumentApi.md#get_document_by_field_document_structured_search_get) | **GET** /document/_structured_search | search documents by descriptive field names
*DocumentApi* | [**get_document_by_syntax_string_document_search_get**](docs/DocumentApi.md#get_document_by_syntax_string_document_search_get) | **GET** /document/_search | search documents by zbMATH style user query
*DocumentApi* | [**get_document_by_zbmath_id_document_id_get**](docs/DocumentApi.md#get_document_by_zbmath_id_document_id_get) | **GET** /document/{id} | get document data by zbMath ID
*DocumentApi* | [**intro_document_get**](docs/DocumentApi.md#intro_document_get) | **GET** /document/ | introduction for user help regarding this endpoint
*SerialApi* | [**get_serial_by_field_serial_structured_search_get**](docs/SerialApi.md#get_serial_by_field_serial_structured_search_get) | **GET** /serial/_structured_search | search serial meta data by descriptive field names
*SerialApi* | [**get_serial_by_id_serial_id_get**](docs/SerialApi.md#get_serial_by_id_serial_id_get) | **GET** /serial/{id} | get serial data by serial id
*SerialApi* | [**get_serial_by_syntax_string_serial_search_get**](docs/SerialApi.md#get_serial_by_syntax_string_serial_search_get) | **GET** /serial/_search | search serial meta data by zbMATH style user query
*SerialApi* | [**intro_serial_get**](docs/SerialApi.md#intro_serial_get) | **GET** /serial/ | introduction for user help regarding this endpoint serial
*SoftwareApi* | [**get_software_by_field_software_structured_search_get**](docs/SoftwareApi.md#get_software_by_field_software_structured_search_get) | **GET** /software/_structured_search | search software meta data by descriptive field names
*SoftwareApi* | [**get_software_by_id_software_id_get**](docs/SoftwareApi.md#get_software_by_id_software_id_get) | **GET** /software/{id} | get software data by software id
*SoftwareApi* | [**get_software_by_syntax_string_software_search_get**](docs/SoftwareApi.md#get_software_by_syntax_string_software_search_get) | **GET** /software/_search | search software meta data by zbMATH style user query
*SoftwareApi* | [**intro_software_get**](docs/SoftwareApi.md#intro_software_get) | **GET** /software/ | introduction for user help regarding this endpoint software

## Documentation For Models

 - [AllOfAwardWikidata](docs/AllOfAwardWikidata.md)
 - [AllOfDocumentContributors](docs/AllOfDocumentContributors.md)
 - [AllOfDocumentLanguage](docs/AllOfDocumentLanguage.md)
 - [AllOfDocumentSource](docs/AllOfDocumentSource.md)
 - [AllOfDocumentTitle](docs/AllOfDocumentTitle.md)
 - [AllOfEditorialContributionReviewer](docs/AllOfEditorialContributionReviewer.md)
 - [AllOfReferenceZbmath](docs/AllOfReferenceZbmath.md)
 - [AllOfSerialLanguages](docs/AllOfSerialLanguages.md)
 - [AllOfSerialLineage](docs/AllOfSerialLineage.md)
 - [AllOfSerialTranslation](docs/AllOfSerialTranslation.md)
 - [AllOfzbmathApiDataModelsDisplayAuthorsResultIDResult](docs/AllOfzbmathApiDataModelsDisplayAuthorsResultIDResult.md)
 - [AllOfzbmathApiDataModelsDisplayAuthorsResultIDStatus](docs/AllOfzbmathApiDataModelsDisplayAuthorsResultIDStatus.md)
 - [AllOfzbmathApiDataModelsDisplayAuthorsResultSearchStatus](docs/AllOfzbmathApiDataModelsDisplayAuthorsResultSearchStatus.md)
 - [AllOfzbmathApiDataModelsDisplayClassificationsResultIDResult](docs/AllOfzbmathApiDataModelsDisplayClassificationsResultIDResult.md)
 - [AllOfzbmathApiDataModelsDisplayClassificationsResultIDStatus](docs/AllOfzbmathApiDataModelsDisplayClassificationsResultIDStatus.md)
 - [AllOfzbmathApiDataModelsDisplayClassificationsResultSearchStatus](docs/AllOfzbmathApiDataModelsDisplayClassificationsResultSearchStatus.md)
 - [AllOfzbmathApiDataModelsDisplayDocumentsResultIDResult](docs/AllOfzbmathApiDataModelsDisplayDocumentsResultIDResult.md)
 - [AllOfzbmathApiDataModelsDisplayDocumentsResultIDStatus](docs/AllOfzbmathApiDataModelsDisplayDocumentsResultIDStatus.md)
 - [AllOfzbmathApiDataModelsDisplayDocumentsResultSearchStatus](docs/AllOfzbmathApiDataModelsDisplayDocumentsResultSearchStatus.md)
 - [AllOfzbmathApiDataModelsDisplaySerialsResultIDResult](docs/AllOfzbmathApiDataModelsDisplaySerialsResultIDResult.md)
 - [AllOfzbmathApiDataModelsDisplaySerialsResultIDStatus](docs/AllOfzbmathApiDataModelsDisplaySerialsResultIDStatus.md)
 - [AllOfzbmathApiDataModelsDisplaySerialsResultSearchStatus](docs/AllOfzbmathApiDataModelsDisplaySerialsResultSearchStatus.md)
 - [AllOfzbmathApiDataModelsDisplaySoftwareResultIDResult](docs/AllOfzbmathApiDataModelsDisplaySoftwareResultIDResult.md)
 - [AllOfzbmathApiDataModelsDisplaySoftwareResultIDStatus](docs/AllOfzbmathApiDataModelsDisplaySoftwareResultIDStatus.md)
 - [AllOfzbmathApiDataModelsDisplaySoftwareResultSearchStatus](docs/AllOfzbmathApiDataModelsDisplaySoftwareResultSearchStatus.md)
 - [AuthorReference](docs/AuthorReference.md)
 - [Award](docs/Award.md)
 - [BiographicReference](docs/BiographicReference.md)
 - [Book](docs/Book.md)
 - [Classification](docs/Classification.md)
 - [ContributionType](docs/ContributionType.md)
 - [Contributor](docs/Contributor.md)
 - [CountryCodes](docs/CountryCodes.md)
 - [Document](docs/Document.md)
 - [DocumentType](docs/DocumentType.md)
 - [Editor](docs/Editor.md)
 - [EditorialContribution](docs/EditorialContribution.md)
 - [ExternalID](docs/ExternalID.md)
 - [ExternalIdType](docs/ExternalIdType.md)
 - [FurtherSpelling](docs/FurtherSpelling.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [ISBN](docs/ISBN.md)
 - [ISSNType](docs/ISSNType.md)
 - [Language](docs/Language.md)
 - [LanguageCodes](docs/LanguageCodes.md)
 - [Languages](docs/Languages.md)
 - [Level](docs/Level.md)
 - [Lineage](docs/Lineage.md)
 - [Link](docs/Link.md)
 - [LinkType](docs/LinkType.md)
 - [MSC](docs/MSC.md)
 - [Reference](docs/Reference.md)
 - [RelatedSoftware](docs/RelatedSoftware.md)
 - [Reviewer](docs/Reviewer.md)
 - [Serial](docs/Serial.md)
 - [SerialType](docs/SerialType.md)
 - [Series](docs/Series.md)
 - [Software](docs/Software.md)
 - [Source](docs/Source.md)
 - [Spelling](docs/Spelling.md)
 - [StandardArticle](docs/StandardArticle.md)
 - [State](docs/State.md)
 - [Status](docs/Status.md)
 - [Title](docs/Title.md)
 - [Translation](docs/Translation.md)
 - [ValidationError](docs/ValidationError.md)
 - [WhichCountry](docs/WhichCountry.md)
 - [WhichLanguage](docs/WhichLanguage.md)
 - [WikiData](docs/WikiData.md)
 - [ZBMath](docs/ZBMath.md)
 - [ZbmathApiDataModelsDisplayAuthorsAuthor](docs/ZbmathApiDataModelsDisplayAuthorsAuthor.md)
 - [ZbmathApiDataModelsDisplayAuthorsResultID](docs/ZbmathApiDataModelsDisplayAuthorsResultID.md)
 - [ZbmathApiDataModelsDisplayAuthorsResultSearch](docs/ZbmathApiDataModelsDisplayAuthorsResultSearch.md)
 - [ZbmathApiDataModelsDisplayAuthorsSubmodelsMainField](docs/ZbmathApiDataModelsDisplayAuthorsSubmodelsMainField.md)
 - [ZbmathApiDataModelsDisplayAuthorsSubmodelsState](docs/ZbmathApiDataModelsDisplayAuthorsSubmodelsState.md)
 - [ZbmathApiDataModelsDisplayClassificationsResultID](docs/ZbmathApiDataModelsDisplayClassificationsResultID.md)
 - [ZbmathApiDataModelsDisplayClassificationsResultSearch](docs/ZbmathApiDataModelsDisplayClassificationsResultSearch.md)
 - [ZbmathApiDataModelsDisplayDocumentsResultID](docs/ZbmathApiDataModelsDisplayDocumentsResultID.md)
 - [ZbmathApiDataModelsDisplayDocumentsResultSearch](docs/ZbmathApiDataModelsDisplayDocumentsResultSearch.md)
 - [ZbmathApiDataModelsDisplayDocumentsSubmodelsAuthor](docs/ZbmathApiDataModelsDisplayDocumentsSubmodelsAuthor.md)
 - [ZbmathApiDataModelsDisplayDocumentsSubmodelsISSN](docs/ZbmathApiDataModelsDisplayDocumentsSubmodelsISSN.md)
 - [ZbmathApiDataModelsDisplayDocumentsSubmodelsISSNType](docs/ZbmathApiDataModelsDisplayDocumentsSubmodelsISSNType.md)
 - [ZbmathApiDataModelsDisplayDocumentsSubmodelsState](docs/ZbmathApiDataModelsDisplayDocumentsSubmodelsState.md)
 - [ZbmathApiDataModelsDisplaySerialsResultID](docs/ZbmathApiDataModelsDisplaySerialsResultID.md)
 - [ZbmathApiDataModelsDisplaySerialsResultSearch](docs/ZbmathApiDataModelsDisplaySerialsResultSearch.md)
 - [ZbmathApiDataModelsDisplaySerialsSubmodelsISSN](docs/ZbmathApiDataModelsDisplaySerialsSubmodelsISSN.md)
 - [ZbmathApiDataModelsDisplaySerialsSubmodelsISSNType](docs/ZbmathApiDataModelsDisplaySerialsSubmodelsISSNType.md)
 - [ZbmathApiDataModelsDisplaySerialsSubmodelsMainField](docs/ZbmathApiDataModelsDisplaySerialsSubmodelsMainField.md)
 - [ZbmathApiDataModelsDisplaySerialsSubmodelsState](docs/ZbmathApiDataModelsDisplaySerialsSubmodelsState.md)
 - [ZbmathApiDataModelsDisplaySoftwareResultID](docs/ZbmathApiDataModelsDisplaySoftwareResultID.md)
 - [ZbmathApiDataModelsDisplaySoftwareResultSearch](docs/ZbmathApiDataModelsDisplaySoftwareResultSearch.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

