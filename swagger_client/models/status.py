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

class Status(object):
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
        'execution': 'str',
        'execution_bool': 'bool',
        'internal_code': 'str',
        'query_execution_time_in_seconds': 'float',
        'status_code': 'int',
        'time_stamp': 'str'
    }

    attribute_map = {
        'execution': 'execution',
        'execution_bool': 'execution_bool',
        'internal_code': 'internal_code',
        'query_execution_time_in_seconds': 'query_execution_time_in_seconds',
        'status_code': 'status_code',
        'time_stamp': 'time_stamp'
    }

    def __init__(self, execution=None, execution_bool=None, internal_code='undefined', query_execution_time_in_seconds=-0.1, status_code=None, time_stamp='undefined'):  # noqa: E501
        """Status - a model defined in Swagger"""  # noqa: E501
        self._execution = None
        self._execution_bool = None
        self._internal_code = None
        self._query_execution_time_in_seconds = None
        self._status_code = None
        self._time_stamp = None
        self.discriminator = None
        self.execution = execution
        self.execution_bool = execution_bool
        if internal_code is not None:
            self.internal_code = internal_code
        if query_execution_time_in_seconds is not None:
            self.query_execution_time_in_seconds = query_execution_time_in_seconds
        self.status_code = status_code
        if time_stamp is not None:
            self.time_stamp = time_stamp

    @property
    def execution(self):
        """Gets the execution of this Status.  # noqa: E501


        :return: The execution of this Status.  # noqa: E501
        :rtype: str
        """
        return self._execution

    @execution.setter
    def execution(self, execution):
        """Sets the execution of this Status.


        :param execution: The execution of this Status.  # noqa: E501
        :type: str
        """
        if execution is None:
            raise ValueError("Invalid value for `execution`, must not be `None`")  # noqa: E501

        self._execution = execution

    @property
    def execution_bool(self):
        """Gets the execution_bool of this Status.  # noqa: E501


        :return: The execution_bool of this Status.  # noqa: E501
        :rtype: bool
        """
        return self._execution_bool

    @execution_bool.setter
    def execution_bool(self, execution_bool):
        """Sets the execution_bool of this Status.


        :param execution_bool: The execution_bool of this Status.  # noqa: E501
        :type: bool
        """
        if execution_bool is None:
            raise ValueError("Invalid value for `execution_bool`, must not be `None`")  # noqa: E501

        self._execution_bool = execution_bool

    @property
    def internal_code(self):
        """Gets the internal_code of this Status.  # noqa: E501


        :return: The internal_code of this Status.  # noqa: E501
        :rtype: str
        """
        return self._internal_code

    @internal_code.setter
    def internal_code(self, internal_code):
        """Sets the internal_code of this Status.


        :param internal_code: The internal_code of this Status.  # noqa: E501
        :type: str
        """

        self._internal_code = internal_code

    @property
    def query_execution_time_in_seconds(self):
        """Gets the query_execution_time_in_seconds of this Status.  # noqa: E501


        :return: The query_execution_time_in_seconds of this Status.  # noqa: E501
        :rtype: float
        """
        return self._query_execution_time_in_seconds

    @query_execution_time_in_seconds.setter
    def query_execution_time_in_seconds(self, query_execution_time_in_seconds):
        """Sets the query_execution_time_in_seconds of this Status.


        :param query_execution_time_in_seconds: The query_execution_time_in_seconds of this Status.  # noqa: E501
        :type: float
        """

        self._query_execution_time_in_seconds = query_execution_time_in_seconds

    @property
    def status_code(self):
        """Gets the status_code of this Status.  # noqa: E501


        :return: The status_code of this Status.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this Status.


        :param status_code: The status_code of this Status.  # noqa: E501
        :type: int
        """
        if status_code is None:
            raise ValueError("Invalid value for `status_code`, must not be `None`")  # noqa: E501

        self._status_code = status_code

    @property
    def time_stamp(self):
        """Gets the time_stamp of this Status.  # noqa: E501


        :return: The time_stamp of this Status.  # noqa: E501
        :rtype: str
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this Status.


        :param time_stamp: The time_stamp of this Status.  # noqa: E501
        :type: str
        """

        self._time_stamp = time_stamp

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
        if issubclass(Status, dict):
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
        if not isinstance(other, Status):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
