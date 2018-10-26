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


class PartStudiosGetShadedViewsResponse200(object):
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
        'images': 'list[str]'
    }

    attribute_map = {
        'images': 'images'
    }

    def __init__(self, images=None):  # noqa: E501
        """PartStudiosGetShadedViewsResponse200 - a model defined in Swagger"""  # noqa: E501

        self._images = None
        self.discriminator = None

        if images is not None:
            self.images = images

    @property
    def images(self):
        """Gets the images of this PartStudiosGetShadedViewsResponse200.  # noqa: E501

        Array of Base64 strings encoding PNG images  # noqa: E501

        :return: The images of this PartStudiosGetShadedViewsResponse200.  # noqa: E501
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this PartStudiosGetShadedViewsResponse200.

        Array of Base64 strings encoding PNG images  # noqa: E501

        :param images: The images of this PartStudiosGetShadedViewsResponse200.  # noqa: E501
        :type: list[str]
        """

        self._images = images

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
        if not isinstance(other, PartStudiosGetShadedViewsResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other