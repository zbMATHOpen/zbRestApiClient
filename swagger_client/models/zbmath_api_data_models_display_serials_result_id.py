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

class ZbmathApiDataModelsDisplaySerialsResultID(object):
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
        'result': 'AllOfzbmathApiDataModelsDisplaySerialsResultIDResult',
        'status': 'AllOfzbmathApiDataModelsDisplaySerialsResultIDStatus'
    }

    attribute_map = {
        'result': 'result',
        'status': 'status'
    }

    def __init__(self, result=None, status=None):  # noqa: E501
        """ZbmathApiDataModelsDisplaySerialsResultID - a model defined in Swagger"""  # noqa: E501
        self._result = None
        self._status = None
        self.discriminator = None
        if result is not None:
            self.result = result
        if status is not None:
            self.status = status

    @property
    def result(self):
        """Gets the result of this ZbmathApiDataModelsDisplaySerialsResultID.  # noqa: E501


        :return: The result of this ZbmathApiDataModelsDisplaySerialsResultID.  # noqa: E501
        :rtype: AllOfzbmathApiDataModelsDisplaySerialsResultIDResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ZbmathApiDataModelsDisplaySerialsResultID.


        :param result: The result of this ZbmathApiDataModelsDisplaySerialsResultID.  # noqa: E501
        :type: AllOfzbmathApiDataModelsDisplaySerialsResultIDResult
        """

        self._result = result

    @property
    def status(self):
        """Gets the status of this ZbmathApiDataModelsDisplaySerialsResultID.  # noqa: E501


        :return: The status of this ZbmathApiDataModelsDisplaySerialsResultID.  # noqa: E501
        :rtype: AllOfzbmathApiDataModelsDisplaySerialsResultIDStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ZbmathApiDataModelsDisplaySerialsResultID.


        :param status: The status of this ZbmathApiDataModelsDisplaySerialsResultID.  # noqa: E501
        :type: AllOfzbmathApiDataModelsDisplaySerialsResultIDStatus
        """

        self._status = status

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
        if issubclass(ZbmathApiDataModelsDisplaySerialsResultID, dict):
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
        if not isinstance(other, ZbmathApiDataModelsDisplaySerialsResultID):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
