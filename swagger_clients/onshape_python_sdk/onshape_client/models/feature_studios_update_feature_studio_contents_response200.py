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


class FeatureStudiosUpdateFeatureStudioContentsResponse200(object):
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
        'serialization_version': 'str',
        'source_microversion': 'str',
        'contents': 'object',
        'microversion_skew': 'bool'
    }

    attribute_map = {
        'serialization_version': 'serializationVersion',
        'source_microversion': 'sourceMicroversion',
        'contents': 'contents',
        'microversion_skew': 'microversionSkew'
    }

    def __init__(self, serialization_version=None, source_microversion=None, contents=None, microversion_skew=None):  # noqa: E501
        """FeatureStudiosUpdateFeatureStudioContentsResponse200 - a model defined in Swagger"""  # noqa: E501

        self._serialization_version = None
        self._source_microversion = None
        self._contents = None
        self._microversion_skew = None
        self.discriminator = None

        if serialization_version is not None:
            self.serialization_version = serialization_version
        if source_microversion is not None:
            self.source_microversion = source_microversion
        if contents is not None:
            self.contents = contents
        if microversion_skew is not None:
            self.microversion_skew = microversion_skew

    @property
    def serialization_version(self):
        """Gets the serialization_version of this FeatureStudiosUpdateFeatureStudioContentsResponse200.  # noqa: E501

        The version of the serialization protocol for the response  # noqa: E501

        :return: The serialization_version of this FeatureStudiosUpdateFeatureStudioContentsResponse200.  # noqa: E501
        :rtype: str
        """
        return self._serialization_version

    @serialization_version.setter
    def serialization_version(self, serialization_version):
        """Sets the serialization_version of this FeatureStudiosUpdateFeatureStudioContentsResponse200.

        The version of the serialization protocol for the response  # noqa: E501

        :param serialization_version: The serialization_version of this FeatureStudiosUpdateFeatureStudioContentsResponse200.  # noqa: E501
        :type: str
        """

        self._serialization_version = serialization_version

    @property
    def source_microversion(self):
        """Gets the source_microversion of this FeatureStudiosUpdateFeatureStudioContentsResponse200.  # noqa: E501

        The document microversion from which the feature was extracted  # noqa: E501

        :return: The source_microversion of this FeatureStudiosUpdateFeatureStudioContentsResponse200.  # noqa: E501
        :rtype: str
        """
        return self._source_microversion

    @source_microversion.setter
    def source_microversion(self, source_microversion):
        """Sets the source_microversion of this FeatureStudiosUpdateFeatureStudioContentsResponse200.

        The document microversion from which the feature was extracted  # noqa: E501

        :param source_microversion: The source_microversion of this FeatureStudiosUpdateFeatureStudioContentsResponse200.  # noqa: E501
        :type: str
        """

        self._source_microversion = source_microversion

    @property
    def contents(self):
        """Gets the contents of this FeatureStudiosUpdateFeatureStudioContentsResponse200.  # noqa: E501

        The actual new contents  # noqa: E501

        :return: The contents of this FeatureStudiosUpdateFeatureStudioContentsResponse200.  # noqa: E501
        :rtype: object
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this FeatureStudiosUpdateFeatureStudioContentsResponse200.

        The actual new contents  # noqa: E501

        :param contents: The contents of this FeatureStudiosUpdateFeatureStudioContentsResponse200.  # noqa: E501
        :type: object
        """

        self._contents = contents

    @property
    def microversion_skew(self):
        """Gets the microversion_skew of this FeatureStudiosUpdateFeatureStudioContentsResponse200.  # noqa: E501

        Set to true if the part studio element had changed since the     sourceMicroversion specified on input.  Applicable only if rejectMicroversionSkew was not set to true  # noqa: E501

        :return: The microversion_skew of this FeatureStudiosUpdateFeatureStudioContentsResponse200.  # noqa: E501
        :rtype: bool
        """
        return self._microversion_skew

    @microversion_skew.setter
    def microversion_skew(self, microversion_skew):
        """Sets the microversion_skew of this FeatureStudiosUpdateFeatureStudioContentsResponse200.

        Set to true if the part studio element had changed since the     sourceMicroversion specified on input.  Applicable only if rejectMicroversionSkew was not set to true  # noqa: E501

        :param microversion_skew: The microversion_skew of this FeatureStudiosUpdateFeatureStudioContentsResponse200.  # noqa: E501
        :type: bool
        """

        self._microversion_skew = microversion_skew

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
        if not isinstance(other, FeatureStudiosUpdateFeatureStudioContentsResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other