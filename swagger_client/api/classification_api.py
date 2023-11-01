# coding: utf-8

"""
    REST API for zbMATH Open

    a REST api for zbMATH Open, currently with endpoints for authors, classifications, documents, serials and software  # noqa: E501

    OpenAPI spec version: v0.4.3rc0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ClassificationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_classification_by_msc2020_code_classification_code_get(self, code, **kwargs):  # noqa: E501
        """get msc2020 code data by code  # noqa: E501

                 # Description                    # About this Endpoint            Use this endpoint if you have an exact msc2020 classification         code in mind. The result will contain only one dataset         corresponding to that code, if entered correctly.            # Example           - **20J05** leads to information about **\"Homological methods in         group theory\"**           # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_classification_by_msc2020_code_classification_code_get(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: (required)
        :return: ZbmathApiDataModelsDisplayClassificationsResultID
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_classification_by_msc2020_code_classification_code_get_with_http_info(code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_classification_by_msc2020_code_classification_code_get_with_http_info(code, **kwargs)  # noqa: E501
            return data

    def get_classification_by_msc2020_code_classification_code_get_with_http_info(self, code, **kwargs):  # noqa: E501
        """get msc2020 code data by code  # noqa: E501

                 # Description                    # About this Endpoint            Use this endpoint if you have an exact msc2020 classification         code in mind. The result will contain only one dataset         corresponding to that code, if entered correctly.            # Example           - **20J05** leads to information about **\"Homological methods in         group theory\"**           # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_classification_by_msc2020_code_classification_code_get_with_http_info(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: (required)
        :return: ZbmathApiDataModelsDisplayClassificationsResultID
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_classification_by_msc2020_code_classification_code_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `get_classification_by_msc2020_code_classification_code_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/classification/{code}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ZbmathApiDataModelsDisplayClassificationsResultID',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_msc2020_by_field_classification_structured_search_get(self, **kwargs):  # noqa: E501
        """search msc codes meta data by descriptive field names  # noqa: E501

                 # Description                    For searching in zbMATH you may employ the Structured Search for         convenient combination of all search fields. While similar to the         1-line syntax search, this endpoint offers much more convenience and         transparency which fields are searched at the cost of search         flexibility.                    # Examples           - **field:** 'code', **term:** '16E20': Search for the msc code         **16E20**.           - **field:** 'code', **term:** '16': Search for all msc codes         start with **16**.           - **field:** 'title', **term:** 'dynamic': Search for all msc codes         containing the descriptor **dynamic**.          # Search fields  - **code**: msc code (2020) - **level**: level of msc code resolution (0,1,2) - **parent**: parent level of msc code - **title**: descriptive title of msc code  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_msc2020_by_field_classification_structured_search_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: result page
        :param int results_per_page:
        :param str code: code
        :param str title: title
        :param str level: level
        :param str parent: parent
        :return: ZbmathApiDataModelsDisplayClassificationsResultSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_msc2020_by_field_classification_structured_search_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_msc2020_by_field_classification_structured_search_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_msc2020_by_field_classification_structured_search_get_with_http_info(self, **kwargs):  # noqa: E501
        """search msc codes meta data by descriptive field names  # noqa: E501

                 # Description                    For searching in zbMATH you may employ the Structured Search for         convenient combination of all search fields. While similar to the         1-line syntax search, this endpoint offers much more convenience and         transparency which fields are searched at the cost of search         flexibility.                    # Examples           - **field:** 'code', **term:** '16E20': Search for the msc code         **16E20**.           - **field:** 'code', **term:** '16': Search for all msc codes         start with **16**.           - **field:** 'title', **term:** 'dynamic': Search for all msc codes         containing the descriptor **dynamic**.          # Search fields  - **code**: msc code (2020) - **level**: level of msc code resolution (0,1,2) - **parent**: parent level of msc code - **title**: descriptive title of msc code  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_msc2020_by_field_classification_structured_search_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: result page
        :param int results_per_page:
        :param str code: code
        :param str title: title
        :param str level: level
        :param str parent: parent
        :return: ZbmathApiDataModelsDisplayClassificationsResultSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'results_per_page', 'code', 'title', 'level', 'parent']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_msc2020_by_field_classification_structured_search_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'results_per_page' in params:
            query_params.append(('results_per_page', params['results_per_page']))  # noqa: E501
        if 'code' in params:
            query_params.append(('code', params['code']))  # noqa: E501
        if 'title' in params:
            query_params.append(('title', params['title']))  # noqa: E501
        if 'level' in params:
            query_params.append(('level', params['level']))  # noqa: E501
        if 'parent' in params:
            query_params.append(('parent', params['parent']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/classification/_structured_search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ZbmathApiDataModelsDisplayClassificationsResultSearch',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_msc2020_by_syntax_string_classification_search_get(self, search_string, **kwargs):  # noqa: E501
        """search msc codes meta data by zbMATH style user query  # noqa: E501

                 # Description                    The syntax search allows for free logical combinations of all         available search fields. While similar to the structured search,         this endpoint offers much more flexibility at the cost of obscure         search parameters.                    # Examples           - **Geometry**: Search for the term Geometry in any field.         Queries are case-independent.          # Search fields  - **cc**: msc code (2020) - **ct**: descriptive title of msc code - **lv**: level of msc code resolution (0,1,2) - **pa**: parent level of msc code            # Operators          - **a & b**: logical and          - **a | b**: logical or          - **!ab**: logical not          - **abc***: right wildcard          - **\"ab c\"**: phrase          - **(ab c)**: parentheses           # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_msc2020_by_syntax_string_classification_search_get(search_string, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_string: (required)
        :param int page:
        :param int results_per_page:
        :return: ZbmathApiDataModelsDisplayClassificationsResultSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_msc2020_by_syntax_string_classification_search_get_with_http_info(search_string, **kwargs)  # noqa: E501
        else:
            (data) = self.get_msc2020_by_syntax_string_classification_search_get_with_http_info(search_string, **kwargs)  # noqa: E501
            return data

    def get_msc2020_by_syntax_string_classification_search_get_with_http_info(self, search_string, **kwargs):  # noqa: E501
        """search msc codes meta data by zbMATH style user query  # noqa: E501

                 # Description                    The syntax search allows for free logical combinations of all         available search fields. While similar to the structured search,         this endpoint offers much more flexibility at the cost of obscure         search parameters.                    # Examples           - **Geometry**: Search for the term Geometry in any field.         Queries are case-independent.          # Search fields  - **cc**: msc code (2020) - **ct**: descriptive title of msc code - **lv**: level of msc code resolution (0,1,2) - **pa**: parent level of msc code            # Operators          - **a & b**: logical and          - **a | b**: logical or          - **!ab**: logical not          - **abc***: right wildcard          - **\"ab c\"**: phrase          - **(ab c)**: parentheses           # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_msc2020_by_syntax_string_classification_search_get_with_http_info(search_string, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_string: (required)
        :param int page:
        :param int results_per_page:
        :return: ZbmathApiDataModelsDisplayClassificationsResultSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_string', 'page', 'results_per_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_msc2020_by_syntax_string_classification_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_string' is set
        if ('search_string' not in params or
                params['search_string'] is None):
            raise ValueError("Missing the required parameter `search_string` when calling `get_msc2020_by_syntax_string_classification_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_string' in params:
            query_params.append(('search_string', params['search_string']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'results_per_page' in params:
            query_params.append(('results_per_page', params['results_per_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/classification/_search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ZbmathApiDataModelsDisplayClassificationsResultSearch',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def intro_classification_get(self, **kwargs):  # noqa: E501
        """introduction for user help regarding this endpoint  # noqa: E501

                # About this Endpoint         For searching in zbMATH you may employ the Structured Search,        which allows for convenient search of all relevant fields.         The syntax search on the other hand allows for free logical        combinations of all available search fields and is much more        flexible. In the following you will find a short explanation of        available search fields.         Use the Classification Search to find information on msc codes of        research fields of interest. msc2020 codes available only.                  **Level 0:** first two digits of msc code         **Level 1:** first two digits plus letter of msc code         **Level 2:** full msc code                           - **/_search**: make use of the zbmath search syntax for complex         search. Examples on how to make use of the syntax can be found in         the endpoint itself.         - **/_structured_search**: a number of fields for a structured search         - **/{msc_code}**: if an identifier for the msc2020 code in        question is available, you man enter it here, to return the meta data        information of just this one msc2020 code.            # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.intro_classification_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.intro_classification_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.intro_classification_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def intro_classification_get_with_http_info(self, **kwargs):  # noqa: E501
        """introduction for user help regarding this endpoint  # noqa: E501

                # About this Endpoint         For searching in zbMATH you may employ the Structured Search,        which allows for convenient search of all relevant fields.         The syntax search on the other hand allows for free logical        combinations of all available search fields and is much more        flexible. In the following you will find a short explanation of        available search fields.         Use the Classification Search to find information on msc codes of        research fields of interest. msc2020 codes available only.                  **Level 0:** first two digits of msc code         **Level 1:** first two digits plus letter of msc code         **Level 2:** full msc code                           - **/_search**: make use of the zbmath search syntax for complex         search. Examples on how to make use of the syntax can be found in         the endpoint itself.         - **/_structured_search**: a number of fields for a structured search         - **/{msc_code}**: if an identifier for the msc2020 code in        question is available, you man enter it here, to return the meta data        information of just this one msc2020 code.            # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.intro_classification_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method intro_classification_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/classification/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)