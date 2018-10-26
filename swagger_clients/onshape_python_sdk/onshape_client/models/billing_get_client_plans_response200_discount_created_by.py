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


class BillingGetClientPlansResponse200DiscountCreatedBy(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'image': 'str',
        'email': 'str',
        'state': 'float',
        'href': 'str',
        'id': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'image': 'image',
        'email': 'email',
        'state': 'state',
        'href': 'href',
        'id': 'id'
    }

    def __init__(self, first_name=None, last_name=None, image=None, email=None, state=None, href=None, id=None):  # noqa: E501
        """BillingGetClientPlansResponse200DiscountCreatedBy - a model defined in Swagger"""  # noqa: E501

        self._first_name = None
        self._last_name = None
        self._image = None
        self._email = None
        self._state = None
        self._href = None
        self._id = None
        self.discriminator = None

        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if image is not None:
            self.image = image
        if email is not None:
            self.email = email
        if state is not None:
            self.state = state
        if href is not None:
            self.href = href
        if id is not None:
            self.id = id

    @property
    def first_name(self):
        """Gets the first_name of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501

        discount creator user first name  # noqa: E501

        :return: The first_name of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this BillingGetClientPlansResponse200DiscountCreatedBy.

        discount creator user first name  # noqa: E501

        :param first_name: The first_name of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501

        discount creator user last name  # noqa: E501

        :return: The last_name of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this BillingGetClientPlansResponse200DiscountCreatedBy.

        discount creator user last name  # noqa: E501

        :param last_name: The last_name of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def image(self):
        """Gets the image of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501

        discount creator user image url  # noqa: E501

        :return: The image of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this BillingGetClientPlansResponse200DiscountCreatedBy.

        discount creator user image url  # noqa: E501

        :param image: The image of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def email(self):
        """Gets the email of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501

        discount creator e-mail  # noqa: E501

        :return: The email of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BillingGetClientPlansResponse200DiscountCreatedBy.

        discount creator e-mail  # noqa: E501

        :param email: The email of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def state(self):
        """Gets the state of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501

        discount creator user state  # noqa: E501

        :return: The state of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501
        :rtype: float
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BillingGetClientPlansResponse200DiscountCreatedBy.

        discount creator user state  # noqa: E501

        :param state: The state of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501
        :type: float
        """

        self._state = state

    @property
    def href(self):
        """Gets the href of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501

        discount creator user href  # noqa: E501

        :return: The href of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BillingGetClientPlansResponse200DiscountCreatedBy.

        discount creator user href  # noqa: E501

        :param href: The href of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501

        discount creator user id  # noqa: E501

        :return: The id of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BillingGetClientPlansResponse200DiscountCreatedBy.

        discount creator user id  # noqa: E501

        :param id: The id of this BillingGetClientPlansResponse200DiscountCreatedBy.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, BillingGetClientPlansResponse200DiscountCreatedBy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other