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

class StandardArticle(object):
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
        'authors': 'list[object]',
        'id': 'int',
        'source': 'str',
        'title': 'str',
        'year': 'str'
    }

    attribute_map = {
        'authors': 'authors',
        'id': 'id',
        'source': 'source',
        'title': 'title',
        'year': 'year'
    }

    def __init__(self, authors=None, id=None, source=None, title=None, year=None):  # noqa: E501
        """StandardArticle - a model defined in Swagger"""  # noqa: E501
        self._authors = None
        self._id = None
        self._source = None
        self._title = None
        self._year = None
        self.discriminator = None
        if authors is not None:
            self.authors = authors
        if id is not None:
            self.id = id
        if source is not None:
            self.source = source
        if title is not None:
            self.title = title
        if year is not None:
            self.year = year

    @property
    def authors(self):
        """Gets the authors of this StandardArticle.  # noqa: E501


        :return: The authors of this StandardArticle.  # noqa: E501
        :rtype: list[object]
        """
        return self._authors

    @authors.setter
    def authors(self, authors):
        """Sets the authors of this StandardArticle.


        :param authors: The authors of this StandardArticle.  # noqa: E501
        :type: list[object]
        """

        self._authors = authors

    @property
    def id(self):
        """Gets the id of this StandardArticle.  # noqa: E501


        :return: The id of this StandardArticle.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StandardArticle.


        :param id: The id of this StandardArticle.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def source(self):
        """Gets the source of this StandardArticle.  # noqa: E501


        :return: The source of this StandardArticle.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this StandardArticle.


        :param source: The source of this StandardArticle.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def title(self):
        """Gets the title of this StandardArticle.  # noqa: E501


        :return: The title of this StandardArticle.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this StandardArticle.


        :param title: The title of this StandardArticle.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def year(self):
        """Gets the year of this StandardArticle.  # noqa: E501


        :return: The year of this StandardArticle.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this StandardArticle.


        :param year: The year of this StandardArticle.  # noqa: E501
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
        if issubclass(StandardArticle, dict):
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
        if not isinstance(other, StandardArticle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other