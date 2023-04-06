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


class RetentionExecution(object):
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
        "id": "int",
        "policy_id": "int",
        "start_time": "str",
        "end_time": "str",
        "status": "str",
        "trigger": "str",
        "dry_run": "bool",
    }

    attribute_map = {
        "id": "id",
        "policy_id": "policy_id",
        "start_time": "start_time",
        "end_time": "end_time",
        "status": "status",
        "trigger": "trigger",
        "dry_run": "dry_run",
    }

    def __init__(
        self,
        id=None,
        policy_id=None,
        start_time=None,
        end_time=None,
        status=None,
        trigger=None,
        dry_run=None,
        _configuration=None,
    ):  # noqa: E501
        """RetentionExecution - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._policy_id = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._trigger = None
        self._dry_run = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policy_id is not None:
            self.policy_id = policy_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if trigger is not None:
            self.trigger = trigger
        if dry_run is not None:
            self.dry_run = dry_run

    @property
    def id(self):
        """Gets the id of this RetentionExecution.  # noqa: E501


        :return: The id of this RetentionExecution.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RetentionExecution.


        :param id: The id of this RetentionExecution.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def policy_id(self):
        """Gets the policy_id of this RetentionExecution.  # noqa: E501


        :return: The policy_id of this RetentionExecution.  # noqa: E501
        :rtype: int
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this RetentionExecution.


        :param policy_id: The policy_id of this RetentionExecution.  # noqa: E501
        :type: int
        """

        self._policy_id = policy_id

    @property
    def start_time(self):
        """Gets the start_time of this RetentionExecution.  # noqa: E501


        :return: The start_time of this RetentionExecution.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this RetentionExecution.


        :param start_time: The start_time of this RetentionExecution.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this RetentionExecution.  # noqa: E501


        :return: The end_time of this RetentionExecution.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this RetentionExecution.


        :param end_time: The end_time of this RetentionExecution.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this RetentionExecution.  # noqa: E501


        :return: The status of this RetentionExecution.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RetentionExecution.


        :param status: The status of this RetentionExecution.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def trigger(self):
        """Gets the trigger of this RetentionExecution.  # noqa: E501


        :return: The trigger of this RetentionExecution.  # noqa: E501
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this RetentionExecution.


        :param trigger: The trigger of this RetentionExecution.  # noqa: E501
        :type: str
        """

        self._trigger = trigger

    @property
    def dry_run(self):
        """Gets the dry_run of this RetentionExecution.  # noqa: E501


        :return: The dry_run of this RetentionExecution.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this RetentionExecution.


        :param dry_run: The dry_run of this RetentionExecution.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

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
        if issubclass(RetentionExecution, dict):
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
        if not isinstance(other, RetentionExecution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RetentionExecution):
            return True

        return self.to_dict() != other.to_dict()
