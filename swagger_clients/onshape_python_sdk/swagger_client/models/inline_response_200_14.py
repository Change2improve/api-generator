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

from swagger_client.models.inline_response20014_items import InlineResponse20014Items  # noqa: F401,E501


class InlineResponse20014(object):
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
        'previous': 'str',
        'href': 'str',
        'next': 'str',
        'items': 'list[InlineResponse20014Items]'
    }

    attribute_map = {
        'previous': 'previous',
        'href': 'href',
        'next': 'next',
        'items': 'items'
    }

    def __init__(self, previous=None, href=None, next=None, items=None):  # noqa: E501
        """InlineResponse20014 - a model defined in Swagger"""  # noqa: E501

        self._previous = None
        self._href = None
        self._next = None
        self._items = None
        self.discriminator = None

        self.previous = previous
        self.href = href
        self.next = next
        self.items = items

    @property
    def previous(self):
        """Gets the previous of this InlineResponse20014.  # noqa: E501

        URL of previous page of results  # noqa: E501

        :return: The previous of this InlineResponse20014.  # noqa: E501
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this InlineResponse20014.

        URL of previous page of results  # noqa: E501

        :param previous: The previous of this InlineResponse20014.  # noqa: E501
        :type: str
        """
        if previous is None:
            raise ValueError("Invalid value for `previous`, must not be `None`")  # noqa: E501

        self._previous = previous

    @property
    def href(self):
        """Gets the href of this InlineResponse20014.  # noqa: E501

        URL of current page of results  # noqa: E501

        :return: The href of this InlineResponse20014.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this InlineResponse20014.

        URL of current page of results  # noqa: E501

        :param href: The href of this InlineResponse20014.  # noqa: E501
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def next(self):
        """Gets the next of this InlineResponse20014.  # noqa: E501

        URL of next page of results  # noqa: E501

        :return: The next of this InlineResponse20014.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this InlineResponse20014.

        URL of next page of results  # noqa: E501

        :param next: The next of this InlineResponse20014.  # noqa: E501
        :type: str
        """
        if next is None:
            raise ValueError("Invalid value for `next`, must not be `None`")  # noqa: E501

        self._next = next

    @property
    def items(self):
        """Gets the items of this InlineResponse20014.  # noqa: E501

        Array of insertables  # noqa: E501

        :return: The items of this InlineResponse20014.  # noqa: E501
        :rtype: list[InlineResponse20014Items]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this InlineResponse20014.

        Array of insertables  # noqa: E501

        :param items: The items of this InlineResponse20014.  # noqa: E501
        :type: list[InlineResponse20014Items]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

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
        if not isinstance(other, InlineResponse20014):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other