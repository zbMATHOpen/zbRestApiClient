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

class Classification(object):
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
        'code': 'str',
        'level': 'Level',
        'long_title': 'str',
        'parent': 'str',
        'short_title': 'str',
        'zbmath_url': 'str',
        'data_source': 'object'
    }

    attribute_map = {
        'code': 'code',
        'level': 'level',
        'long_title': 'long_title',
        'parent': 'parent',
        'short_title': 'short_title',
        'zbmath_url': 'zbmath_url',
        'data_source': 'data_source'
    }

    def __init__(self, code=None, level=None, long_title=None, parent=None, short_title=None, zbmath_url=None, data_source=None):  # noqa: E501
        """Classification - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._level = None
        self._long_title = None
        self._parent = None
        self._short_title = None
        self._zbmath_url = None
        self._data_source = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if level is not None:
            self.level = level
        if long_title is not None:
            self.long_title = long_title
        if parent is not None:
            self.parent = parent
        if short_title is not None:
            self.short_title = short_title
        if zbmath_url is not None:
            self.zbmath_url = zbmath_url
        if data_source is not None:
            self.data_source = data_source

    @property
    def code(self):
        """Gets the code of this Classification.  # noqa: E501


        :return: The code of this Classification.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Classification.


        :param code: The code of this Classification.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def level(self):
        """Gets the level of this Classification.  # noqa: E501


        :return: The level of this Classification.  # noqa: E501
        :rtype: Level
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this Classification.


        :param level: The level of this Classification.  # noqa: E501
        :type: Level
        """

        self._level = level

    @property
    def long_title(self):
        """Gets the long_title of this Classification.  # noqa: E501


        :return: The long_title of this Classification.  # noqa: E501
        :rtype: str
        """
        return self._long_title

    @long_title.setter
    def long_title(self, long_title):
        """Sets the long_title of this Classification.


        :param long_title: The long_title of this Classification.  # noqa: E501
        :type: str
        """

        self._long_title = long_title

    @property
    def parent(self):
        """Gets the parent of this Classification.  # noqa: E501


        :return: The parent of this Classification.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this Classification.


        :param parent: The parent of this Classification.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def short_title(self):
        """Gets the short_title of this Classification.  # noqa: E501


        :return: The short_title of this Classification.  # noqa: E501
        :rtype: str
        """
        return self._short_title

    @short_title.setter
    def short_title(self, short_title):
        """Sets the short_title of this Classification.


        :param short_title: The short_title of this Classification.  # noqa: E501
        :type: str
        """

        self._short_title = short_title

    @property
    def zbmath_url(self):
        """Gets the zbmath_url of this Classification.  # noqa: E501


        :return: The zbmath_url of this Classification.  # noqa: E501
        :rtype: str
        """
        return self._zbmath_url

    @zbmath_url.setter
    def zbmath_url(self, zbmath_url):
        """Sets the zbmath_url of this Classification.


        :param zbmath_url: The zbmath_url of this Classification.  # noqa: E501
        :type: str
        """

        self._zbmath_url = zbmath_url

    @property
    def data_source(self):
        """Gets the data_source of this Classification.  # noqa: E501


        :return: The data_source of this Classification.  # noqa: E501
        :rtype: object
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this Classification.


        :param data_source: The data_source of this Classification.  # noqa: E501
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
        if issubclass(Classification, dict):
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
        if not isinstance(other, Classification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
