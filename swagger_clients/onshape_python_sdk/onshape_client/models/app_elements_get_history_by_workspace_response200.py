# coding: utf-8

"""
    Onshape API

    Onshape API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: ekeller@onshape.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from onshape_client.models.app_elements_get_history_by_workspace_response200_changes import AppElementsGetHistoryByWorkspaceResponse200Changes  # noqa: F401,E501


class AppElementsGetHistoryByWorkspaceResponse200(object):
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
        'changes': 'list[AppElementsGetHistoryByWorkspaceResponse200Changes]'
    }

    attribute_map = {
        'changes': 'changes'
    }

    def __init__(self, changes=None):  # noqa: E501
        """AppElementsGetHistoryByWorkspaceResponse200 - a model defined in Swagger"""  # noqa: E501

        self._changes = None
        self.discriminator = None

        if changes is not None:
            self.changes = changes

    @property
    def changes(self):
        """Gets the changes of this AppElementsGetHistoryByWorkspaceResponse200.  # noqa: E501

        List of subelement history entries in order of more recent to less   recent  # noqa: E501

        :return: The changes of this AppElementsGetHistoryByWorkspaceResponse200.  # noqa: E501
        :rtype: list[AppElementsGetHistoryByWorkspaceResponse200Changes]
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """Sets the changes of this AppElementsGetHistoryByWorkspaceResponse200.

        List of subelement history entries in order of more recent to less   recent  # noqa: E501

        :param changes: The changes of this AppElementsGetHistoryByWorkspaceResponse200.  # noqa: E501
        :type: list[AppElementsGetHistoryByWorkspaceResponse200Changes]
        """

        self._changes = changes

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AppElementsGetHistoryByWorkspaceResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other