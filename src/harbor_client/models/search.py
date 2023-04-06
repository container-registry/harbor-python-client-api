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


class Search(object):
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
        "project": "list[Project]",
        "repository": "list[SearchRepository]",
        "chart": "list[SearchResult]",
    }

    attribute_map = {"project": "project", "repository": "repository", "chart": "chart"}

    def __init__(
        self, project=None, repository=None, chart=None, _configuration=None
    ):  # noqa: E501
        """Search - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._project = None
        self._repository = None
        self._chart = None
        self.discriminator = None

        if project is not None:
            self.project = project
        if repository is not None:
            self.repository = repository
        if chart is not None:
            self.chart = chart

    @property
    def project(self):
        """Gets the project of this Search.  # noqa: E501

        Search results of the projects that matched the filter keywords.  # noqa: E501

        :return: The project of this Search.  # noqa: E501
        :rtype: list[Project]
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Search.

        Search results of the projects that matched the filter keywords.  # noqa: E501

        :param project: The project of this Search.  # noqa: E501
        :type: list[Project]
        """

        self._project = project

    @property
    def repository(self):
        """Gets the repository of this Search.  # noqa: E501

        Search results of the repositories that matched the filter keywords.  # noqa: E501

        :return: The repository of this Search.  # noqa: E501
        :rtype: list[SearchRepository]
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this Search.

        Search results of the repositories that matched the filter keywords.  # noqa: E501

        :param repository: The repository of this Search.  # noqa: E501
        :type: list[SearchRepository]
        """

        self._repository = repository

    @property
    def chart(self):
        """Gets the chart of this Search.  # noqa: E501

        Search results of the charts that macthed the filter keywords.  # noqa: E501

        :return: The chart of this Search.  # noqa: E501
        :rtype: list[SearchResult]
        """
        return self._chart

    @chart.setter
    def chart(self, chart):
        """Sets the chart of this Search.

        Search results of the charts that macthed the filter keywords.  # noqa: E501

        :param chart: The chart of this Search.  # noqa: E501
        :type: list[SearchResult]
        """

        self._chart = chart

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
        if issubclass(Search, dict):
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
        if not isinstance(other, Search):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Search):
            return True

        return self.to_dict() != other.to_dict()
