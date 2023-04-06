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


class WebhookJob(object):
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
        "event_type": "str",
        "notify_type": "str",
        "status": "str",
        "job_detail": "str",
        "creation_time": "datetime",
        "update_time": "datetime",
    }

    attribute_map = {
        "id": "id",
        "policy_id": "policy_id",
        "event_type": "event_type",
        "notify_type": "notify_type",
        "status": "status",
        "job_detail": "job_detail",
        "creation_time": "creation_time",
        "update_time": "update_time",
    }

    def __init__(
        self,
        id=None,
        policy_id=None,
        event_type=None,
        notify_type=None,
        status=None,
        job_detail=None,
        creation_time=None,
        update_time=None,
        _configuration=None,
    ):  # noqa: E501
        """WebhookJob - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._policy_id = None
        self._event_type = None
        self._notify_type = None
        self._status = None
        self._job_detail = None
        self._creation_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policy_id is not None:
            self.policy_id = policy_id
        if event_type is not None:
            self.event_type = event_type
        if notify_type is not None:
            self.notify_type = notify_type
        if status is not None:
            self.status = status
        if job_detail is not None:
            self.job_detail = job_detail
        if creation_time is not None:
            self.creation_time = creation_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this WebhookJob.  # noqa: E501

        The webhook job ID.  # noqa: E501

        :return: The id of this WebhookJob.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookJob.

        The webhook job ID.  # noqa: E501

        :param id: The id of this WebhookJob.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def policy_id(self):
        """Gets the policy_id of this WebhookJob.  # noqa: E501

        The webhook policy ID.  # noqa: E501

        :return: The policy_id of this WebhookJob.  # noqa: E501
        :rtype: int
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this WebhookJob.

        The webhook policy ID.  # noqa: E501

        :param policy_id: The policy_id of this WebhookJob.  # noqa: E501
        :type: int
        """

        self._policy_id = policy_id

    @property
    def event_type(self):
        """Gets the event_type of this WebhookJob.  # noqa: E501

        The webhook job event type.  # noqa: E501

        :return: The event_type of this WebhookJob.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this WebhookJob.

        The webhook job event type.  # noqa: E501

        :param event_type: The event_type of this WebhookJob.  # noqa: E501
        :type: str
        """

        self._event_type = event_type

    @property
    def notify_type(self):
        """Gets the notify_type of this WebhookJob.  # noqa: E501

        The webhook job notify type.  # noqa: E501

        :return: The notify_type of this WebhookJob.  # noqa: E501
        :rtype: str
        """
        return self._notify_type

    @notify_type.setter
    def notify_type(self, notify_type):
        """Sets the notify_type of this WebhookJob.

        The webhook job notify type.  # noqa: E501

        :param notify_type: The notify_type of this WebhookJob.  # noqa: E501
        :type: str
        """

        self._notify_type = notify_type

    @property
    def status(self):
        """Gets the status of this WebhookJob.  # noqa: E501

        The webhook job status.  # noqa: E501

        :return: The status of this WebhookJob.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WebhookJob.

        The webhook job status.  # noqa: E501

        :param status: The status of this WebhookJob.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def job_detail(self):
        """Gets the job_detail of this WebhookJob.  # noqa: E501

        The webhook job notify detailed data.  # noqa: E501

        :return: The job_detail of this WebhookJob.  # noqa: E501
        :rtype: str
        """
        return self._job_detail

    @job_detail.setter
    def job_detail(self, job_detail):
        """Sets the job_detail of this WebhookJob.

        The webhook job notify detailed data.  # noqa: E501

        :param job_detail: The job_detail of this WebhookJob.  # noqa: E501
        :type: str
        """

        self._job_detail = job_detail

    @property
    def creation_time(self):
        """Gets the creation_time of this WebhookJob.  # noqa: E501

        The webhook job creation time.  # noqa: E501

        :return: The creation_time of this WebhookJob.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this WebhookJob.

        The webhook job creation time.  # noqa: E501

        :param creation_time: The creation_time of this WebhookJob.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def update_time(self):
        """Gets the update_time of this WebhookJob.  # noqa: E501

        The webhook job update time.  # noqa: E501

        :return: The update_time of this WebhookJob.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this WebhookJob.

        The webhook job update time.  # noqa: E501

        :param update_time: The update_time of this WebhookJob.  # noqa: E501
        :type: datetime
        """

        self._update_time = update_time

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
        if issubclass(WebhookJob, dict):
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
        if not isinstance(other, WebhookJob):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookJob):
            return True

        return self.to_dict() != other.to_dict()
