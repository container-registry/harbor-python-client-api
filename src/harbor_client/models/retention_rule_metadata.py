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


class RetentionRuleMetadata(object):
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
        "rule_template": "str",
        "display_text": "str",
        "action": "str",
        "params": "list[RetentionRuleParamMetadata]",
    }

    attribute_map = {
        "rule_template": "rule_template",
        "display_text": "display_text",
        "action": "action",
        "params": "params",
    }

    def __init__(
        self, rule_template=None, display_text=None, action=None, params=None, _configuration=None
    ):  # noqa: E501
        """RetentionRuleMetadata - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._rule_template = None
        self._display_text = None
        self._action = None
        self._params = None
        self.discriminator = None

        if rule_template is not None:
            self.rule_template = rule_template
        if display_text is not None:
            self.display_text = display_text
        if action is not None:
            self.action = action
        if params is not None:
            self.params = params

    @property
    def rule_template(self):
        """Gets the rule_template of this RetentionRuleMetadata.  # noqa: E501

        rule id  # noqa: E501

        :return: The rule_template of this RetentionRuleMetadata.  # noqa: E501
        :rtype: str
        """
        return self._rule_template

    @rule_template.setter
    def rule_template(self, rule_template):
        """Sets the rule_template of this RetentionRuleMetadata.

        rule id  # noqa: E501

        :param rule_template: The rule_template of this RetentionRuleMetadata.  # noqa: E501
        :type: str
        """

        self._rule_template = rule_template

    @property
    def display_text(self):
        """Gets the display_text of this RetentionRuleMetadata.  # noqa: E501

        rule display text  # noqa: E501

        :return: The display_text of this RetentionRuleMetadata.  # noqa: E501
        :rtype: str
        """
        return self._display_text

    @display_text.setter
    def display_text(self, display_text):
        """Sets the display_text of this RetentionRuleMetadata.

        rule display text  # noqa: E501

        :param display_text: The display_text of this RetentionRuleMetadata.  # noqa: E501
        :type: str
        """

        self._display_text = display_text

    @property
    def action(self):
        """Gets the action of this RetentionRuleMetadata.  # noqa: E501

        rule action  # noqa: E501

        :return: The action of this RetentionRuleMetadata.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this RetentionRuleMetadata.

        rule action  # noqa: E501

        :param action: The action of this RetentionRuleMetadata.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def params(self):
        """Gets the params of this RetentionRuleMetadata.  # noqa: E501

        rule params  # noqa: E501

        :return: The params of this RetentionRuleMetadata.  # noqa: E501
        :rtype: list[RetentionRuleParamMetadata]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this RetentionRuleMetadata.

        rule params  # noqa: E501

        :param params: The params of this RetentionRuleMetadata.  # noqa: E501
        :type: list[RetentionRuleParamMetadata]
        """

        self._params = params

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
        if issubclass(RetentionRuleMetadata, dict):
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
        if not isinstance(other, RetentionRuleMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RetentionRuleMetadata):
            return True

        return self.to_dict() != other.to_dict()
