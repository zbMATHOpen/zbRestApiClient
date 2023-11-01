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

class Book(object):
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
        'book_id': 'int',
        'isbn': 'list[ISBN]',
        'publisher': 'str',
        'year': 'str'
    }

    attribute_map = {
        'book_id': 'book_id',
        'isbn': 'isbn',
        'publisher': 'publisher',
        'year': 'year'
    }

    def __init__(self, book_id=None, isbn=None, publisher=None, year=None):  # noqa: E501
        """Book - a model defined in Swagger"""  # noqa: E501
        self._book_id = None
        self._isbn = None
        self._publisher = None
        self._year = None
        self.discriminator = None
        if book_id is not None:
            self.book_id = book_id
        if isbn is not None:
            self.isbn = isbn
        if publisher is not None:
            self.publisher = publisher
        if year is not None:
            self.year = year

    @property
    def book_id(self):
        """Gets the book_id of this Book.  # noqa: E501


        :return: The book_id of this Book.  # noqa: E501
        :rtype: int
        """
        return self._book_id

    @book_id.setter
    def book_id(self, book_id):
        """Sets the book_id of this Book.


        :param book_id: The book_id of this Book.  # noqa: E501
        :type: int
        """

        self._book_id = book_id

    @property
    def isbn(self):
        """Gets the isbn of this Book.  # noqa: E501


        :return: The isbn of this Book.  # noqa: E501
        :rtype: list[ISBN]
        """
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        """Sets the isbn of this Book.


        :param isbn: The isbn of this Book.  # noqa: E501
        :type: list[ISBN]
        """

        self._isbn = isbn

    @property
    def publisher(self):
        """Gets the publisher of this Book.  # noqa: E501


        :return: The publisher of this Book.  # noqa: E501
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this Book.


        :param publisher: The publisher of this Book.  # noqa: E501
        :type: str
        """

        self._publisher = publisher

    @property
    def year(self):
        """Gets the year of this Book.  # noqa: E501


        :return: The year of this Book.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this Book.


        :param year: The year of this Book.  # noqa: E501
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
        if issubclass(Book, dict):
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
        if not isinstance(other, Book):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
