# coding: utf-8

"""
    REST API for zbMATH Open

    a REST api for zbMATH Open, currently with endpoints for authors, classifications, documents, serials and software  # noqa: E501

    OpenAPI spec version: v0.4.3rc0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Serial(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'acronym': 'str',
        'comments': 'list[object]',
        'countries': 'list[WhichCountry]',
        'id': 'int',
        'issn': 'list[ZbmathApiDataModelsDisplaySerialsSubmodelsISSN]',
        'languages': 'AllOfSerialLanguages',
        'lineage': 'AllOfSerialLineage',
        'main_fields': 'list[ZbmathApiDataModelsDisplaySerialsSubmodelsMainField]',
        'online_availability': 'str',
        'parallel_title': 'str',
        'publisher': 'str',
        'serial_type': 'SerialType',
        'short_title': 'str',
        'states': 'list[State]',
        'sub_series': 'list[object]',
        'sub_title': 'str',
        'title': 'str',
        'translation': 'AllOfSerialTranslation',
        'urls': 'list[object]',
        'zbmath_start': 'str',
        'zbmath_stop': 'str',
        'zbmath_years': 'list[object]',
        'zbmath_url': 'str',
        'data_source': 'object'
    }

    attribute_map = {
        'acronym': 'acronym',
        'comments': 'comments',
        'countries': 'countries',
        'id': 'id',
        'issn': 'issn',
        'languages': 'languages',
        'lineage': 'lineage',
        'main_fields': 'main_fields',
        'online_availability': 'online_availability',
        'parallel_title': 'parallel_title',
        'publisher': 'publisher',
        'serial_type': 'serial_type',
        'short_title': 'short_title',
        'states': 'states',
        'sub_series': 'sub_series',
        'sub_title': 'sub_title',
        'title': 'title',
        'translation': 'translation',
        'urls': 'urls',
        'zbmath_start': 'zbmath_start',
        'zbmath_stop': 'zbmath_stop',
        'zbmath_years': 'zbmath_years',
        'zbmath_url': 'zbmath_url',
        'data_source': 'data_source'
    }

    def __init__(self, acronym=None, comments=None, countries=None, id=None, issn=None, languages=None, lineage=None, main_fields=None, online_availability=None, parallel_title=None, publisher=None, serial_type=None, short_title=None, states=None, sub_series=None, sub_title=None, title=None, translation=None, urls=None, zbmath_start=None, zbmath_stop=None, zbmath_years=None, zbmath_url=None, data_source=None):  # noqa: E501
        """Serial - a model defined in Swagger"""  # noqa: E501
        self._acronym = None
        self._comments = None
        self._countries = None
        self._id = None
        self._issn = None
        self._languages = None
        self._lineage = None
        self._main_fields = None
        self._online_availability = None
        self._parallel_title = None
        self._publisher = None
        self._serial_type = None
        self._short_title = None
        self._states = None
        self._sub_series = None
        self._sub_title = None
        self._title = None
        self._translation = None
        self._urls = None
        self._zbmath_start = None
        self._zbmath_stop = None
        self._zbmath_years = None
        self._zbmath_url = None
        self._data_source = None
        self.discriminator = None
        if acronym is not None:
            self.acronym = acronym
        if comments is not None:
            self.comments = comments
        if countries is not None:
            self.countries = countries
        if id is not None:
            self.id = id
        if issn is not None:
            self.issn = issn
        if languages is not None:
            self.languages = languages
        if lineage is not None:
            self.lineage = lineage
        if main_fields is not None:
            self.main_fields = main_fields
        if online_availability is not None:
            self.online_availability = online_availability
        if parallel_title is not None:
            self.parallel_title = parallel_title
        if publisher is not None:
            self.publisher = publisher
        if serial_type is not None:
            self.serial_type = serial_type
        if short_title is not None:
            self.short_title = short_title
        if states is not None:
            self.states = states
        if sub_series is not None:
            self.sub_series = sub_series
        if sub_title is not None:
            self.sub_title = sub_title
        if title is not None:
            self.title = title
        if translation is not None:
            self.translation = translation
        if urls is not None:
            self.urls = urls
        if zbmath_start is not None:
            self.zbmath_start = zbmath_start
        if zbmath_stop is not None:
            self.zbmath_stop = zbmath_stop
        if zbmath_years is not None:
            self.zbmath_years = zbmath_years
        if zbmath_url is not None:
            self.zbmath_url = zbmath_url
        if data_source is not None:
            self.data_source = data_source

    @property
    def acronym(self):
        """Gets the acronym of this Serial.  # noqa: E501


        :return: The acronym of this Serial.  # noqa: E501
        :rtype: str
        """
        return self._acronym

    @acronym.setter
    def acronym(self, acronym):
        """Sets the acronym of this Serial.


        :param acronym: The acronym of this Serial.  # noqa: E501
        :type: str
        """

        self._acronym = acronym

    @property
    def comments(self):
        """Gets the comments of this Serial.  # noqa: E501


        :return: The comments of this Serial.  # noqa: E501
        :rtype: list[object]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this Serial.


        :param comments: The comments of this Serial.  # noqa: E501
        :type: list[object]
        """

        self._comments = comments

    @property
    def countries(self):
        """Gets the countries of this Serial.  # noqa: E501


        :return: The countries of this Serial.  # noqa: E501
        :rtype: list[WhichCountry]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """Sets the countries of this Serial.


        :param countries: The countries of this Serial.  # noqa: E501
        :type: list[WhichCountry]
        """

        self._countries = countries

    @property
    def id(self):
        """Gets the id of this Serial.  # noqa: E501


        :return: The id of this Serial.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Serial.


        :param id: The id of this Serial.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def issn(self):
        """Gets the issn of this Serial.  # noqa: E501


        :return: The issn of this Serial.  # noqa: E501
        :rtype: list[ZbmathApiDataModelsDisplaySerialsSubmodelsISSN]
        """
        return self._issn

    @issn.setter
    def issn(self, issn):
        """Sets the issn of this Serial.


        :param issn: The issn of this Serial.  # noqa: E501
        :type: list[ZbmathApiDataModelsDisplaySerialsSubmodelsISSN]
        """

        self._issn = issn

    @property
    def languages(self):
        """Gets the languages of this Serial.  # noqa: E501


        :return: The languages of this Serial.  # noqa: E501
        :rtype: AllOfSerialLanguages
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """Sets the languages of this Serial.


        :param languages: The languages of this Serial.  # noqa: E501
        :type: AllOfSerialLanguages
        """

        self._languages = languages

    @property
    def lineage(self):
        """Gets the lineage of this Serial.  # noqa: E501


        :return: The lineage of this Serial.  # noqa: E501
        :rtype: AllOfSerialLineage
        """
        return self._lineage

    @lineage.setter
    def lineage(self, lineage):
        """Sets the lineage of this Serial.


        :param lineage: The lineage of this Serial.  # noqa: E501
        :type: AllOfSerialLineage
        """

        self._lineage = lineage

    @property
    def main_fields(self):
        """Gets the main_fields of this Serial.  # noqa: E501


        :return: The main_fields of this Serial.  # noqa: E501
        :rtype: list[ZbmathApiDataModelsDisplaySerialsSubmodelsMainField]
        """
        return self._main_fields

    @main_fields.setter
    def main_fields(self, main_fields):
        """Sets the main_fields of this Serial.


        :param main_fields: The main_fields of this Serial.  # noqa: E501
        :type: list[ZbmathApiDataModelsDisplaySerialsSubmodelsMainField]
        """

        self._main_fields = main_fields

    @property
    def online_availability(self):
        """Gets the online_availability of this Serial.  # noqa: E501


        :return: The online_availability of this Serial.  # noqa: E501
        :rtype: str
        """
        return self._online_availability

    @online_availability.setter
    def online_availability(self, online_availability):
        """Sets the online_availability of this Serial.


        :param online_availability: The online_availability of this Serial.  # noqa: E501
        :type: str
        """

        self._online_availability = online_availability

    @property
    def parallel_title(self):
        """Gets the parallel_title of this Serial.  # noqa: E501


        :return: The parallel_title of this Serial.  # noqa: E501
        :rtype: str
        """
        return self._parallel_title

    @parallel_title.setter
    def parallel_title(self, parallel_title):
        """Sets the parallel_title of this Serial.


        :param parallel_title: The parallel_title of this Serial.  # noqa: E501
        :type: str
        """

        self._parallel_title = parallel_title

    @property
    def publisher(self):
        """Gets the publisher of this Serial.  # noqa: E501


        :return: The publisher of this Serial.  # noqa: E501
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this Serial.


        :param publisher: The publisher of this Serial.  # noqa: E501
        :type: str
        """

        self._publisher = publisher

    @property
    def serial_type(self):
        """Gets the serial_type of this Serial.  # noqa: E501


        :return: The serial_type of this Serial.  # noqa: E501
        :rtype: SerialType
        """
        return self._serial_type

    @serial_type.setter
    def serial_type(self, serial_type):
        """Sets the serial_type of this Serial.


        :param serial_type: The serial_type of this Serial.  # noqa: E501
        :type: SerialType
        """

        self._serial_type = serial_type

    @property
    def short_title(self):
        """Gets the short_title of this Serial.  # noqa: E501


        :return: The short_title of this Serial.  # noqa: E501
        :rtype: str
        """
        return self._short_title

    @short_title.setter
    def short_title(self, short_title):
        """Sets the short_title of this Serial.


        :param short_title: The short_title of this Serial.  # noqa: E501
        :type: str
        """

        self._short_title = short_title

    @property
    def states(self):
        """Gets the states of this Serial.  # noqa: E501


        :return: The states of this Serial.  # noqa: E501
        :rtype: list[State]
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this Serial.


        :param states: The states of this Serial.  # noqa: E501
        :type: list[State]
        """

        self._states = states

    @property
    def sub_series(self):
        """Gets the sub_series of this Serial.  # noqa: E501


        :return: The sub_series of this Serial.  # noqa: E501
        :rtype: list[object]
        """
        return self._sub_series

    @sub_series.setter
    def sub_series(self, sub_series):
        """Sets the sub_series of this Serial.


        :param sub_series: The sub_series of this Serial.  # noqa: E501
        :type: list[object]
        """

        self._sub_series = sub_series

    @property
    def sub_title(self):
        """Gets the sub_title of this Serial.  # noqa: E501


        :return: The sub_title of this Serial.  # noqa: E501
        :rtype: str
        """
        return self._sub_title

    @sub_title.setter
    def sub_title(self, sub_title):
        """Sets the sub_title of this Serial.


        :param sub_title: The sub_title of this Serial.  # noqa: E501
        :type: str
        """

        self._sub_title = sub_title

    @property
    def title(self):
        """Gets the title of this Serial.  # noqa: E501


        :return: The title of this Serial.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Serial.


        :param title: The title of this Serial.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def translation(self):
        """Gets the translation of this Serial.  # noqa: E501


        :return: The translation of this Serial.  # noqa: E501
        :rtype: AllOfSerialTranslation
        """
        return self._translation

    @translation.setter
    def translation(self, translation):
        """Sets the translation of this Serial.


        :param translation: The translation of this Serial.  # noqa: E501
        :type: AllOfSerialTranslation
        """

        self._translation = translation

    @property
    def urls(self):
        """Gets the urls of this Serial.  # noqa: E501


        :return: The urls of this Serial.  # noqa: E501
        :rtype: list[object]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this Serial.


        :param urls: The urls of this Serial.  # noqa: E501
        :type: list[object]
        """

        self._urls = urls

    @property
    def zbmath_start(self):
        """Gets the zbmath_start of this Serial.  # noqa: E501


        :return: The zbmath_start of this Serial.  # noqa: E501
        :rtype: str
        """
        return self._zbmath_start

    @zbmath_start.setter
    def zbmath_start(self, zbmath_start):
        """Sets the zbmath_start of this Serial.


        :param zbmath_start: The zbmath_start of this Serial.  # noqa: E501
        :type: str
        """

        self._zbmath_start = zbmath_start

    @property
    def zbmath_stop(self):
        """Gets the zbmath_stop of this Serial.  # noqa: E501


        :return: The zbmath_stop of this Serial.  # noqa: E501
        :rtype: str
        """
        return self._zbmath_stop

    @zbmath_stop.setter
    def zbmath_stop(self, zbmath_stop):
        """Sets the zbmath_stop of this Serial.


        :param zbmath_stop: The zbmath_stop of this Serial.  # noqa: E501
        :type: str
        """

        self._zbmath_stop = zbmath_stop

    @property
    def zbmath_years(self):
        """Gets the zbmath_years of this Serial.  # noqa: E501


        :return: The zbmath_years of this Serial.  # noqa: E501
        :rtype: list[object]
        """
        return self._zbmath_years

    @zbmath_years.setter
    def zbmath_years(self, zbmath_years):
        """Sets the zbmath_years of this Serial.


        :param zbmath_years: The zbmath_years of this Serial.  # noqa: E501
        :type: list[object]
        """

        self._zbmath_years = zbmath_years

    @property
    def zbmath_url(self):
        """Gets the zbmath_url of this Serial.  # noqa: E501


        :return: The zbmath_url of this Serial.  # noqa: E501
        :rtype: str
        """
        return self._zbmath_url

    @zbmath_url.setter
    def zbmath_url(self, zbmath_url):
        """Sets the zbmath_url of this Serial.


        :param zbmath_url: The zbmath_url of this Serial.  # noqa: E501
        :type: str
        """

        self._zbmath_url = zbmath_url

    @property
    def data_source(self):
        """Gets the data_source of this Serial.  # noqa: E501


        :return: The data_source of this Serial.  # noqa: E501
        :rtype: object
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this Serial.


        :param data_source: The data_source of this Serial.  # noqa: E501
        :type: object
        """

        self._data_source = data_source

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Serial, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Serial):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other