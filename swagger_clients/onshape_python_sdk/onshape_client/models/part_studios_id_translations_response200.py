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

from onshape_client.models.part_studios_id_translations_response200_ids import PartStudiosIdTranslationsResponse200Ids  # noqa: F401,E501


class PartStudiosIdTranslationsResponse200(object):
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
        'source_configuration': 'str',
        'source_document_microversion': 'str',
        'ids': 'list[PartStudiosIdTranslationsResponse200Ids]',
        'target_configuration': 'str',
        'document_id': 'str',
        'target_document_microversion': 'str',
        'element_id': 'str'
    }

    attribute_map = {
        'source_configuration': 'sourceConfiguration',
        'source_document_microversion': 'sourceDocumentMicroversion',
        'ids': 'ids',
        'target_configuration': 'targetConfiguration',
        'document_id': 'documentId',
        'target_document_microversion': 'targetDocumentMicroversion',
        'element_id': 'elementId'
    }

    def __init__(self, source_configuration=None, source_document_microversion=None, ids=None, target_configuration=None, document_id=None, target_document_microversion=None, element_id=None):  # noqa: E501
        """PartStudiosIdTranslationsResponse200 - a model defined in Swagger"""  # noqa: E501

        self._source_configuration = None
        self._source_document_microversion = None
        self._ids = None
        self._target_configuration = None
        self._document_id = None
        self._target_document_microversion = None
        self._element_id = None
        self.discriminator = None

        if source_configuration is not None:
            self.source_configuration = source_configuration
        if source_document_microversion is not None:
            self.source_document_microversion = source_document_microversion
        if ids is not None:
            self.ids = ids
        if target_configuration is not None:
            self.target_configuration = target_configuration
        if document_id is not None:
            self.document_id = document_id
        if target_document_microversion is not None:
            self.target_document_microversion = target_document_microversion
        if element_id is not None:
            self.element_id = element_id

    @property
    def source_configuration(self):
        """Gets the source_configuration of this PartStudiosIdTranslationsResponse200.  # noqa: E501

        Configuration of part studio in which ids were acquired  # noqa: E501

        :return: The source_configuration of this PartStudiosIdTranslationsResponse200.  # noqa: E501
        :rtype: str
        """
        return self._source_configuration

    @source_configuration.setter
    def source_configuration(self, source_configuration):
        """Sets the source_configuration of this PartStudiosIdTranslationsResponse200.

        Configuration of part studio in which ids were acquired  # noqa: E501

        :param source_configuration: The source_configuration of this PartStudiosIdTranslationsResponse200.  # noqa: E501
        :type: str
        """

        self._source_configuration = source_configuration

    @property
    def source_document_microversion(self):
        """Gets the source_document_microversion of this PartStudiosIdTranslationsResponse200.  # noqa: E501

        Source document microversion  # noqa: E501

        :return: The source_document_microversion of this PartStudiosIdTranslationsResponse200.  # noqa: E501
        :rtype: str
        """
        return self._source_document_microversion

    @source_document_microversion.setter
    def source_document_microversion(self, source_document_microversion):
        """Sets the source_document_microversion of this PartStudiosIdTranslationsResponse200.

        Source document microversion  # noqa: E501

        :param source_document_microversion: The source_document_microversion of this PartStudiosIdTranslationsResponse200.  # noqa: E501
        :type: str
        """

        self._source_document_microversion = source_document_microversion

    @property
    def ids(self):
        """Gets the ids of this PartStudiosIdTranslationsResponse200.  # noqa: E501

        Array of id translation results  # noqa: E501

        :return: The ids of this PartStudiosIdTranslationsResponse200.  # noqa: E501
        :rtype: list[PartStudiosIdTranslationsResponse200Ids]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this PartStudiosIdTranslationsResponse200.

        Array of id translation results  # noqa: E501

        :param ids: The ids of this PartStudiosIdTranslationsResponse200.  # noqa: E501
        :type: list[PartStudiosIdTranslationsResponse200Ids]
        """

        self._ids = ids

    @property
    def target_configuration(self):
        """Gets the target_configuration of this PartStudiosIdTranslationsResponse200.  # noqa: E501

        Configuration of part studio into which ids are to be             translated  # noqa: E501

        :return: The target_configuration of this PartStudiosIdTranslationsResponse200.  # noqa: E501
        :rtype: str
        """
        return self._target_configuration

    @target_configuration.setter
    def target_configuration(self, target_configuration):
        """Sets the target_configuration of this PartStudiosIdTranslationsResponse200.

        Configuration of part studio into which ids are to be             translated  # noqa: E501

        :param target_configuration: The target_configuration of this PartStudiosIdTranslationsResponse200.  # noqa: E501
        :type: str
        """

        self._target_configuration = target_configuration

    @property
    def document_id(self):
        """Gets the document_id of this PartStudiosIdTranslationsResponse200.  # noqa: E501

        Document id  # noqa: E501

        :return: The document_id of this PartStudiosIdTranslationsResponse200.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this PartStudiosIdTranslationsResponse200.

        Document id  # noqa: E501

        :param document_id: The document_id of this PartStudiosIdTranslationsResponse200.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def target_document_microversion(self):
        """Gets the target_document_microversion of this PartStudiosIdTranslationsResponse200.  # noqa: E501

        Target document microversion  # noqa: E501

        :return: The target_document_microversion of this PartStudiosIdTranslationsResponse200.  # noqa: E501
        :rtype: str
        """
        return self._target_document_microversion

    @target_document_microversion.setter
    def target_document_microversion(self, target_document_microversion):
        """Sets the target_document_microversion of this PartStudiosIdTranslationsResponse200.

        Target document microversion  # noqa: E501

        :param target_document_microversion: The target_document_microversion of this PartStudiosIdTranslationsResponse200.  # noqa: E501
        :type: str
        """

        self._target_document_microversion = target_document_microversion

    @property
    def element_id(self):
        """Gets the element_id of this PartStudiosIdTranslationsResponse200.  # noqa: E501

        Element id  # noqa: E501

        :return: The element_id of this PartStudiosIdTranslationsResponse200.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this PartStudiosIdTranslationsResponse200.

        Element id  # noqa: E501

        :param element_id: The element_id of this PartStudiosIdTranslationsResponse200.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

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
        if not isinstance(other, PartStudiosIdTranslationsResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other