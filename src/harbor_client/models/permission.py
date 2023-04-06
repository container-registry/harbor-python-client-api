# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from harbor_client.configuration import Configuration


class Permission(object):
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
    swagger_types = {"resource": "str", "action": "str"}

    attribute_map = {"resource": "resource", "action": "action"}

    def __init__(self, resource=None, action=None, _configuration=None):  # noqa: E501
        """Permission - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._resource = None
        self._action = None
        self.discriminator = None

        if resource is not None:
            self.resource = resource
        if action is not None:
            self.action = action

    @property
    def resource(self):
        """Gets the resource of this Permission.  # noqa: E501

        The permission resoruce  # noqa: E501

        :return: The resource of this Permission.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this Permission.

        The permission resoruce  # noqa: E501

        :param resource: The resource of this Permission.  # noqa: E501
        :type: str
        """

        self._resource = resource

    @property
    def action(self):
        """Gets the action of this Permission.  # noqa: E501

        The permission action  # noqa: E501

        :return: The action of this Permission.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Permission.

        The permission action  # noqa: E501

        :param action: The action of this Permission.  # noqa: E501
        :type: str
        """

        self._action = action

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(Permission, dict):
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
        if not isinstance(other, Permission):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Permission):
            return True

        return self.to_dict() != other.to_dict()
