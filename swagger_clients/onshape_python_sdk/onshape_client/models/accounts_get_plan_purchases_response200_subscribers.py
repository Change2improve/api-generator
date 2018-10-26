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


class AccountsGetPlanPurchasesResponse200Subscribers(object):
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
        'last_name': 'object',
        'email': 'object',
        'id': 'object',
        'first_name': 'object',
        'name': 'object'
    }

    attribute_map = {
        'last_name': 'lastName',
        'email': 'email',
        'id': 'id',
        'first_name': 'firstName',
        'name': 'name'
    }

    def __init__(self, last_name=None, email=None, id=None, first_name=None, name=None):  # noqa: E501
        """AccountsGetPlanPurchasesResponse200Subscribers - a model defined in Swagger"""  # noqa: E501

        self._last_name = None
        self._email = None
        self._id = None
        self._first_name = None
        self._name = None
        self.discriminator = None

        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email
        if id is not None:
            self.id = id
        if first_name is not None:
            self.first_name = first_name
        if name is not None:
            self.name = name

    @property
    def last_name(self):
        """Gets the last_name of this AccountsGetPlanPurchasesResponse200Subscribers.  # noqa: E501

        User's last name (requires OAuth2ReadPII scope)  # noqa: E501

        :return: The last_name of this AccountsGetPlanPurchasesResponse200Subscribers.  # noqa: E501
        :rtype: object
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this AccountsGetPlanPurchasesResponse200Subscribers.

        User's last name (requires OAuth2ReadPII scope)  # noqa: E501

        :param last_name: The last_name of this AccountsGetPlanPurchasesResponse200Subscribers.  # noqa: E501
        :type: object
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this AccountsGetPlanPurchasesResponse200Subscribers.  # noqa: E501

        User's email (requires OAuth2ReadPII scope)  # noqa: E501

        :return: The email of this AccountsGetPlanPurchasesResponse200Subscribers.  # noqa: E501
        :rtype: object
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AccountsGetPlanPurchasesResponse200Subscribers.

        User's email (requires OAuth2ReadPII scope)  # noqa: E501

        :param email: The email of this AccountsGetPlanPurchasesResponse200Subscribers.  # noqa: E501
        :type: object
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this AccountsGetPlanPurchasesResponse200Subscribers.  # noqa: E501

        User id  # noqa: E501

        :return: The id of this AccountsGetPlanPurchasesResponse200Subscribers.  # noqa: E501
        :rtype: object
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountsGetPlanPurchasesResponse200Subscribers.

        User id  # noqa: E501

        :param id: The id of this AccountsGetPlanPurchasesResponse200Subscribers.  # noqa: E501
        :type: object
        """

        self._id = id

    @property
    def first_name(self):
        """Gets the first_name of this AccountsGetPlanPurchasesResponse200Subscribers.  # noqa: E501

        User's first name (requires OAuth2ReadPII scope)  # noqa: E501

        :return: The first_name of this AccountsGetPlanPurchasesResponse200Subscribers.  # noqa: E501
        :rtype: object
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this AccountsGetPlanPurchasesResponse200Subscribers.

        User's first name (requires OAuth2ReadPII scope)  # noqa: E501

        :param first_name: The first_name of this AccountsGetPlanPurchasesResponse200Subscribers.  # noqa: E501
        :type: object
        """

        self._first_name = first_name

    @property
    def name(self):
        """Gets the name of this AccountsGetPlanPurchasesResponse200Subscribers.  # noqa: E501

        User's name (requires OAuth2ReadPII scope)  # noqa: E501

        :return: The name of this AccountsGetPlanPurchasesResponse200Subscribers.  # noqa: E501
        :rtype: object
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountsGetPlanPurchasesResponse200Subscribers.

        User's name (requires OAuth2ReadPII scope)  # noqa: E501

        :param name: The name of this AccountsGetPlanPurchasesResponse200Subscribers.  # noqa: E501
        :type: object
        """

        self._name = name

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
        if not isinstance(other, AccountsGetPlanPurchasesResponse200Subscribers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other