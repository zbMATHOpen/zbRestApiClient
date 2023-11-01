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


class SerialApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_serial_by_field_serial_structured_search_get(self, **kwargs):  # noqa: E501
        """search serial meta data by descriptive field names  # noqa: E501

                 # Description                    For searching in zbMATH you may employ the Structured Search for         convenient combination of all search fields. While similar to the         1-line syntax search, this endpoint offers much more convenience and         transparency which fields are searched at the cost of search         flexibility.                    # Examples           - field: 'title', term: 'Annals of Mathematics': Search for         journal title phrase.           - field: 'year', term: '1800-1899': Search for 19th century serials          # Search fields  - **country**: country - **issn**: issn - **language**: language - **main_field**: main fields - **publisher**: publisher - **serial_type**: serial_type - **state**: state - **title**: title - **url**: related url - **year**: year of publishing (range of year possible: XXXX-YYYY)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_serial_by_field_serial_structured_search_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: pagination for result page
        :param int results_per_page:
        :param str country: country
        :param str issn: issn
        :param str language: language
        :param str main_field: main_field
        :param str publisher: publisher
        :param str state: state
        :param str serial_type: serial_type
        :param str title: title
        :param str url: url
        :param str year: year
        :return: ZbmathApiDataModelsDisplaySerialsResultSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_serial_by_field_serial_structured_search_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_serial_by_field_serial_structured_search_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_serial_by_field_serial_structured_search_get_with_http_info(self, **kwargs):  # noqa: E501
        """search serial meta data by descriptive field names  # noqa: E501

                 # Description                    For searching in zbMATH you may employ the Structured Search for         convenient combination of all search fields. While similar to the         1-line syntax search, this endpoint offers much more convenience and         transparency which fields are searched at the cost of search         flexibility.                    # Examples           - field: 'title', term: 'Annals of Mathematics': Search for         journal title phrase.           - field: 'year', term: '1800-1899': Search for 19th century serials          # Search fields  - **country**: country - **issn**: issn - **language**: language - **main_field**: main fields - **publisher**: publisher - **serial_type**: serial_type - **state**: state - **title**: title - **url**: related url - **year**: year of publishing (range of year possible: XXXX-YYYY)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_serial_by_field_serial_structured_search_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: pagination for result page
        :param int results_per_page:
        :param str country: country
        :param str issn: issn
        :param str language: language
        :param str main_field: main_field
        :param str publisher: publisher
        :param str state: state
        :param str serial_type: serial_type
        :param str title: title
        :param str url: url
        :param str year: year
        :return: ZbmathApiDataModelsDisplaySerialsResultSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'results_per_page', 'country', 'issn', 'language', 'main_field', 'publisher', 'state', 'serial_type', 'title', 'url', 'year']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_serial_by_field_serial_structured_search_get" % key
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
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501
        if 'issn' in params:
            query_params.append(('issn', params['issn']))  # noqa: E501
        if 'language' in params:
            query_params.append(('language', params['language']))  # noqa: E501
        if 'main_field' in params:
            query_params.append(('main_field', params['main_field']))  # noqa: E501
        if 'publisher' in params:
            query_params.append(('publisher', params['publisher']))  # noqa: E501
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
        if 'serial_type' in params:
            query_params.append(('serial_type', params['serial_type']))  # noqa: E501
        if 'title' in params:
            query_params.append(('title', params['title']))  # noqa: E501
        if 'url' in params:
            query_params.append(('url', params['url']))  # noqa: E501
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501

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
            '/serial/_structured_search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ZbmathApiDataModelsDisplaySerialsResultSearch',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_serial_by_id_serial_id_get(self, id, **kwargs):  # noqa: E501
        """get serial data by serial id  # noqa: E501

                 # Description                    # About this Endpoint            Use this endpoint if you have the exact zbMATH id of the serial in         question. The result will contain only one dataset corresponding to         that id, if entered correctly.            # Example           - **3191**: leads to information about serial **\"Advances in         Difference Equations\"**           # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_serial_by_id_serial_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: ZbmathApiDataModelsDisplaySerialsResultID
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_serial_by_id_serial_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_serial_by_id_serial_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_serial_by_id_serial_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """get serial data by serial id  # noqa: E501

                 # Description                    # About this Endpoint            Use this endpoint if you have the exact zbMATH id of the serial in         question. The result will contain only one dataset corresponding to         that id, if entered correctly.            # Example           - **3191**: leads to information about serial **\"Advances in         Difference Equations\"**           # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_serial_by_id_serial_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: ZbmathApiDataModelsDisplaySerialsResultID
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_serial_by_id_serial_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_serial_by_id_serial_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/serial/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ZbmathApiDataModelsDisplaySerialsResultID',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_serial_by_syntax_string_serial_search_get(self, search_string, **kwargs):  # noqa: E501
        """search serial meta data by zbMATH style user query  # noqa: E501

                 # Description                    The syntax search allows for free logical combinations of all         available search fields. While similar to the structured search,         this endpoint offers much more flexibility at the cost of obscure         search parameters.                    # Examples           - **Ann\\* Math***: Search for the expressions in all fields.         Abbreviations are also possible.           - **jt:\"Annals of Mathematics\"**: Search for journal title phrase.           - **jt:annals pu:mathematics**: Search for title and publisher.           - **sn:0003-486X**: Search for ISSN. Both electronic and print ISSN         are accepted.           - **se:00002531**: Search for the exact serial identifier. This         excludes homonyms. Compare to jt:Annals of Mathematics.           - **jt:Annals cc:05**: Search for title and main field.           - **jt:Annals (cy:cn | ro)**: Search for title and country.           - **tp:j st:o v t**: Search for journals which are open access and         currently indexed cover-to-cover.           - **py:1800-1899 la:no**: Search for 19th century serials which         published in Norwegian.          # Search fields  - **cc**: main fields - **cy**: country - **jt**: title - **la**: language - **li**: related url - **pu**: publisher - **py**: year of publishing (range of year possible: XXXX-YYYY) - **sn**: issn - **st**: state - **tp**: serial_type            # Operators          - **a & b**: logical and          - **a | b**: logical or          - **!ab**: logical not          - **abc***: right wildcard          - **\"ab c\"**: phrase          - **(ab c)**: parentheses           # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_serial_by_syntax_string_serial_search_get(search_string, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_string: (required)
        :param int page:
        :param int results_per_page:
        :return: ZbmathApiDataModelsDisplaySerialsResultSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_serial_by_syntax_string_serial_search_get_with_http_info(search_string, **kwargs)  # noqa: E501
        else:
            (data) = self.get_serial_by_syntax_string_serial_search_get_with_http_info(search_string, **kwargs)  # noqa: E501
            return data

    def get_serial_by_syntax_string_serial_search_get_with_http_info(self, search_string, **kwargs):  # noqa: E501
        """search serial meta data by zbMATH style user query  # noqa: E501

                 # Description                    The syntax search allows for free logical combinations of all         available search fields. While similar to the structured search,         this endpoint offers much more flexibility at the cost of obscure         search parameters.                    # Examples           - **Ann\\* Math***: Search for the expressions in all fields.         Abbreviations are also possible.           - **jt:\"Annals of Mathematics\"**: Search for journal title phrase.           - **jt:annals pu:mathematics**: Search for title and publisher.           - **sn:0003-486X**: Search for ISSN. Both electronic and print ISSN         are accepted.           - **se:00002531**: Search for the exact serial identifier. This         excludes homonyms. Compare to jt:Annals of Mathematics.           - **jt:Annals cc:05**: Search for title and main field.           - **jt:Annals (cy:cn | ro)**: Search for title and country.           - **tp:j st:o v t**: Search for journals which are open access and         currently indexed cover-to-cover.           - **py:1800-1899 la:no**: Search for 19th century serials which         published in Norwegian.          # Search fields  - **cc**: main fields - **cy**: country - **jt**: title - **la**: language - **li**: related url - **pu**: publisher - **py**: year of publishing (range of year possible: XXXX-YYYY) - **sn**: issn - **st**: state - **tp**: serial_type            # Operators          - **a & b**: logical and          - **a | b**: logical or          - **!ab**: logical not          - **abc***: right wildcard          - **\"ab c\"**: phrase          - **(ab c)**: parentheses           # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_serial_by_syntax_string_serial_search_get_with_http_info(search_string, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_string: (required)
        :param int page:
        :param int results_per_page:
        :return: ZbmathApiDataModelsDisplaySerialsResultSearch
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
                    " to method get_serial_by_syntax_string_serial_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_string' is set
        if ('search_string' not in params or
                params['search_string'] is None):
            raise ValueError("Missing the required parameter `search_string` when calling `get_serial_by_syntax_string_serial_search_get`")  # noqa: E501

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
            '/serial/_search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ZbmathApiDataModelsDisplaySerialsResultSearch',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def intro_serial_get(self, **kwargs):  # noqa: E501
        """introduction for user help regarding this endpoint serial  # noqa: E501

                  # About this Endpoint           For searching in zbMATH you may employ the Structured Search,         which allows for convenient search of all relevant fields.           The syntax search on the other hand allows for free logical         combinations of all available search fields and is much more         flexible. In the following you will find a short explanation of         available search fields.           Use the Serials Search to find information on journals or book         serial. Serial profiles include indexed publications, volume lists,         frequent authors and subjects, open access status, and citation profile.                    - **/_search**: make use of the zbMATH search syntax for complex         search. Examples on how to make use of the syntax can be found in         the endpoint itself.          - **/_structured_search**: a number of fields for a structured search          - **/{id}**: if a zbMATH id for the software in question is         available, you man enter it here, to return the meta data         information of just this one serial entry.            # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.intro_serial_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.intro_serial_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.intro_serial_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def intro_serial_get_with_http_info(self, **kwargs):  # noqa: E501
        """introduction for user help regarding this endpoint serial  # noqa: E501

                  # About this Endpoint           For searching in zbMATH you may employ the Structured Search,         which allows for convenient search of all relevant fields.           The syntax search on the other hand allows for free logical         combinations of all available search fields and is much more         flexible. In the following you will find a short explanation of         available search fields.           Use the Serials Search to find information on journals or book         serial. Serial profiles include indexed publications, volume lists,         frequent authors and subjects, open access status, and citation profile.                    - **/_search**: make use of the zbMATH search syntax for complex         search. Examples on how to make use of the syntax can be found in         the endpoint itself.          - **/_structured_search**: a number of fields for a structured search          - **/{id}**: if a zbMATH id for the software in question is         available, you man enter it here, to return the meta data         information of just this one serial entry.            # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.intro_serial_get_with_http_info(async_req=True)
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
                    " to method intro_serial_get" % key
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
            '/serial/', 'GET',
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