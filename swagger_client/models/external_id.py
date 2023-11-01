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

class ExternalID(object):
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
        'external_id': 'str',
        'type': 'ExternalIdType'
    }

    attribute_map = {
        'external_id': 'external_id',
        'type': 'type'
    }

    def __init__(self, external_id=None, type=None):  # noqa: E501
        """ExternalID - a model defined in Swagger"""  # noqa: E501
        self._external_id = None
        self._type = None
        self.discriminator = None
        if external_id is not None:
            self.external_id = external_id
        if type is not None:
            self.type = type

    @property
    def external_id(self):
        """Gets the external_id of this ExternalID.  # noqa: E501


        :return: The external_id of this ExternalID.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this ExternalID.


        :param external_id: The external_id of this ExternalID.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def type(self):
        """Gets the type of this ExternalID.  # noqa: E501


        :return: The type of this ExternalID.  # noqa: E501
        :rtype: ExternalIdType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExternalID.


        :param type: The type of this ExternalID.  # noqa: E501
        :type: ExternalIdType
        """

        self._type = type

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
        if issubclass(ExternalID, dict):
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
        if not isinstance(other, ExternalID):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
