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

class Contributor(object):
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
        'authors': 'list[ZbmathApiDataModelsDisplayDocumentsSubmodelsAuthor]',
        'author_references': 'list[AuthorReference]',
        'editors': 'list[Editor]'
    }

    attribute_map = {
        'authors': 'authors',
        'author_references': 'author_references',
        'editors': 'editors'
    }

    def __init__(self, authors=None, author_references=None, editors=None):  # noqa: E501
        """Contributor - a model defined in Swagger"""  # noqa: E501
        self._authors = None
        self._author_references = None
        self._editors = None
        self.discriminator = None
        if authors is not None:
            self.authors = authors
        if author_references is not None:
            self.author_references = author_references
        if editors is not None:
            self.editors = editors

    @property
    def authors(self):
        """Gets the authors of this Contributor.  # noqa: E501


        :return: The authors of this Contributor.  # noqa: E501
        :rtype: list[ZbmathApiDataModelsDisplayDocumentsSubmodelsAuthor]
        """
        return self._authors

    @authors.setter
    def authors(self, authors):
        """Sets the authors of this Contributor.


        :param authors: The authors of this Contributor.  # noqa: E501
        :type: list[ZbmathApiDataModelsDisplayDocumentsSubmodelsAuthor]
        """

        self._authors = authors

    @property
    def author_references(self):
        """Gets the author_references of this Contributor.  # noqa: E501


        :return: The author_references of this Contributor.  # noqa: E501
        :rtype: list[AuthorReference]
        """
        return self._author_references

    @author_references.setter
    def author_references(self, author_references):
        """Sets the author_references of this Contributor.


        :param author_references: The author_references of this Contributor.  # noqa: E501
        :type: list[AuthorReference]
        """

        self._author_references = author_references

    @property
    def editors(self):
        """Gets the editors of this Contributor.  # noqa: E501


        :return: The editors of this Contributor.  # noqa: E501
        :rtype: list[Editor]
        """
        return self._editors

    @editors.setter
    def editors(self, editors):
        """Sets the editors of this Contributor.


        :param editors: The editors of this Contributor.  # noqa: E501
        :type: list[Editor]
        """

        self._editors = editors

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
        if issubclass(Contributor, dict):
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
        if not isinstance(other, Contributor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
