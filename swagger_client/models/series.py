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

class Series(object):
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
        'issn': 'list[ZbmathApiDataModelsDisplayDocumentsSubmodelsISSN]',
        'issue': 'str',
        'issue_id': 'int',
        'parallel_title': 'str',
        'part': 'str',
        'publisher': 'str',
        'series_id': 'int',
        'short_title': 'str',
        'title': 'str',
        'volume': 'str',
        'year': 'str'
    }

    attribute_map = {
        'acronym': 'acronym',
        'issn': 'issn',
        'issue': 'issue',
        'issue_id': 'issue_id',
        'parallel_title': 'parallel_title',
        'part': 'part',
        'publisher': 'publisher',
        'series_id': 'series_id',
        'short_title': 'short_title',
        'title': 'title',
        'volume': 'volume',
        'year': 'year'
    }

    def __init__(self, acronym=None, issn=None, issue=None, issue_id=None, parallel_title=None, part=None, publisher=None, series_id=None, short_title=None, title=None, volume=None, year=None):  # noqa: E501
        """Series - a model defined in Swagger"""  # noqa: E501
        self._acronym = None
        self._issn = None
        self._issue = None
        self._issue_id = None
        self._parallel_title = None
        self._part = None
        self._publisher = None
        self._series_id = None
        self._short_title = None
        self._title = None
        self._volume = None
        self._year = None
        self.discriminator = None
        if acronym is not None:
            self.acronym = acronym
        if issn is not None:
            self.issn = issn
        if issue is not None:
            self.issue = issue
        if issue_id is not None:
            self.issue_id = issue_id
        if parallel_title is not None:
            self.parallel_title = parallel_title
        if part is not None:
            self.part = part
        if publisher is not None:
            self.publisher = publisher
        if series_id is not None:
            self.series_id = series_id
        if short_title is not None:
            self.short_title = short_title
        if title is not None:
            self.title = title
        if volume is not None:
            self.volume = volume
        if year is not None:
            self.year = year

    @property
    def acronym(self):
        """Gets the acronym of this Series.  # noqa: E501


        :return: The acronym of this Series.  # noqa: E501
        :rtype: str
        """
        return self._acronym

    @acronym.setter
    def acronym(self, acronym):
        """Sets the acronym of this Series.


        :param acronym: The acronym of this Series.  # noqa: E501
        :type: str
        """

        self._acronym = acronym

    @property
    def issn(self):
        """Gets the issn of this Series.  # noqa: E501


        :return: The issn of this Series.  # noqa: E501
        :rtype: list[ZbmathApiDataModelsDisplayDocumentsSubmodelsISSN]
        """
        return self._issn

    @issn.setter
    def issn(self, issn):
        """Sets the issn of this Series.


        :param issn: The issn of this Series.  # noqa: E501
        :type: list[ZbmathApiDataModelsDisplayDocumentsSubmodelsISSN]
        """

        self._issn = issn

    @property
    def issue(self):
        """Gets the issue of this Series.  # noqa: E501


        :return: The issue of this Series.  # noqa: E501
        :rtype: str
        """
        return self._issue

    @issue.setter
    def issue(self, issue):
        """Sets the issue of this Series.


        :param issue: The issue of this Series.  # noqa: E501
        :type: str
        """

        self._issue = issue

    @property
    def issue_id(self):
        """Gets the issue_id of this Series.  # noqa: E501


        :return: The issue_id of this Series.  # noqa: E501
        :rtype: int
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        """Sets the issue_id of this Series.


        :param issue_id: The issue_id of this Series.  # noqa: E501
        :type: int
        """

        self._issue_id = issue_id

    @property
    def parallel_title(self):
        """Gets the parallel_title of this Series.  # noqa: E501


        :return: The parallel_title of this Series.  # noqa: E501
        :rtype: str
        """
        return self._parallel_title

    @parallel_title.setter
    def parallel_title(self, parallel_title):
        """Sets the parallel_title of this Series.


        :param parallel_title: The parallel_title of this Series.  # noqa: E501
        :type: str
        """

        self._parallel_title = parallel_title

    @property
    def part(self):
        """Gets the part of this Series.  # noqa: E501


        :return: The part of this Series.  # noqa: E501
        :rtype: str
        """
        return self._part

    @part.setter
    def part(self, part):
        """Sets the part of this Series.


        :param part: The part of this Series.  # noqa: E501
        :type: str
        """

        self._part = part

    @property
    def publisher(self):
        """Gets the publisher of this Series.  # noqa: E501


        :return: The publisher of this Series.  # noqa: E501
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this Series.


        :param publisher: The publisher of this Series.  # noqa: E501
        :type: str
        """

        self._publisher = publisher

    @property
    def series_id(self):
        """Gets the series_id of this Series.  # noqa: E501


        :return: The series_id of this Series.  # noqa: E501
        :rtype: int
        """
        return self._series_id

    @series_id.setter
    def series_id(self, series_id):
        """Sets the series_id of this Series.


        :param series_id: The series_id of this Series.  # noqa: E501
        :type: int
        """

        self._series_id = series_id

    @property
    def short_title(self):
        """Gets the short_title of this Series.  # noqa: E501


        :return: The short_title of this Series.  # noqa: E501
        :rtype: str
        """
        return self._short_title

    @short_title.setter
    def short_title(self, short_title):
        """Sets the short_title of this Series.


        :param short_title: The short_title of this Series.  # noqa: E501
        :type: str
        """

        self._short_title = short_title

    @property
    def title(self):
        """Gets the title of this Series.  # noqa: E501


        :return: The title of this Series.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Series.


        :param title: The title of this Series.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def volume(self):
        """Gets the volume of this Series.  # noqa: E501


        :return: The volume of this Series.  # noqa: E501
        :rtype: str
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this Series.


        :param volume: The volume of this Series.  # noqa: E501
        :type: str
        """

        self._volume = volume

    @property
    def year(self):
        """Gets the year of this Series.  # noqa: E501


        :return: The year of this Series.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this Series.


        :param year: The year of this Series.  # noqa: E501
        :type: str
        """

        self._year = year

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
        if issubclass(Series, dict):
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
        if not isinstance(other, Series):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
