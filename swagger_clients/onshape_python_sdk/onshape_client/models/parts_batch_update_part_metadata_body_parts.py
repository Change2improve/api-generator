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

from onshape_client.models.parts_batch_update_part_metadata_body_appearance import PartsBatchUpdatePartMetadataBodyAppearance  # noqa: F401,E501
from onshape_client.models.parts_batch_update_part_metadata_body_material import PartsBatchUpdatePartMetadataBodyMaterial  # noqa: F401,E501
from onshape_client.models.parts_update_part_metadata_body_custom_properties import PartsUpdatePartMetadataBodyCustomProperties  # noqa: F401,E501


class PartsBatchUpdatePartMetadataBodyParts(object):
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
        'vendor': 'str',
        'description': 'str',
        'part_id': 'str',
        'material': 'PartsBatchUpdatePartMetadataBodyMaterial',
        'appearance': 'PartsBatchUpdatePartMetadataBodyAppearance',
        'project': 'str',
        'title1': 'str',
        'title2': 'str',
        'title3': 'str',
        'custom_properties': 'list[PartsUpdatePartMetadataBodyCustomProperties]',
        'product_line': 'str',
        'part_number': 'str',
        'configuration': 'str',
        'revision': 'str',
        'element_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'vendor': 'vendor',
        'description': 'description',
        'part_id': 'partId',
        'material': 'material',
        'appearance': 'appearance',
        'project': 'project',
        'title1': 'title1',
        'title2': 'title2',
        'title3': 'title3',
        'custom_properties': 'customProperties',
        'product_line': 'productLine',
        'part_number': 'partNumber',
        'configuration': 'configuration',
        'revision': 'revision',
        'element_id': 'elementId',
        'name': 'name'
    }

    def __init__(self, vendor=None, description=None, part_id=None, material=None, appearance=None, project=None, title1=None, title2=None, title3=None, custom_properties=None, product_line=None, part_number=None, configuration=None, revision=None, element_id=None, name=None):  # noqa: E501
        """PartsBatchUpdatePartMetadataBodyParts - a model defined in Swagger"""  # noqa: E501

        self._vendor = None
        self._description = None
        self._part_id = None
        self._material = None
        self._appearance = None
        self._project = None
        self._title1 = None
        self._title2 = None
        self._title3 = None
        self._custom_properties = None
        self._product_line = None
        self._part_number = None
        self._configuration = None
        self._revision = None
        self._element_id = None
        self._name = None
        self.discriminator = None

        if vendor is not None:
            self.vendor = vendor
        if description is not None:
            self.description = description
        if part_id is not None:
            self.part_id = part_id
        if material is not None:
            self.material = material
        if appearance is not None:
            self.appearance = appearance
        if project is not None:
            self.project = project
        if title1 is not None:
            self.title1 = title1
        if title2 is not None:
            self.title2 = title2
        if title3 is not None:
            self.title3 = title3
        if custom_properties is not None:
            self.custom_properties = custom_properties
        if product_line is not None:
            self.product_line = product_line
        if part_number is not None:
            self.part_number = part_number
        if configuration is not None:
            self.configuration = configuration
        if revision is not None:
            self.revision = revision
        if element_id is not None:
            self.element_id = element_id
        if name is not None:
            self.name = name

    @property
    def vendor(self):
        """Gets the vendor of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501

        Part vendor  # noqa: E501

        :return: The vendor of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this PartsBatchUpdatePartMetadataBodyParts.

        Part vendor  # noqa: E501

        :param vendor: The vendor of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    @property
    def description(self):
        """Gets the description of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501

        Part description  # noqa: E501

        :return: The description of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PartsBatchUpdatePartMetadataBodyParts.

        Part description  # noqa: E501

        :param description: The description of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def part_id(self):
        """Gets the part_id of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501

        Deterministic part ID of the part to update  # noqa: E501

        :return: The part_id of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :rtype: str
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id):
        """Sets the part_id of this PartsBatchUpdatePartMetadataBodyParts.

        Deterministic part ID of the part to update  # noqa: E501

        :param part_id: The part_id of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :type: str
        """

        self._part_id = part_id

    @property
    def material(self):
        """Gets the material of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501


        :return: The material of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :rtype: PartsBatchUpdatePartMetadataBodyMaterial
        """
        return self._material

    @material.setter
    def material(self, material):
        """Sets the material of this PartsBatchUpdatePartMetadataBodyParts.


        :param material: The material of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :type: PartsBatchUpdatePartMetadataBodyMaterial
        """

        self._material = material

    @property
    def appearance(self):
        """Gets the appearance of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501


        :return: The appearance of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :rtype: PartsBatchUpdatePartMetadataBodyAppearance
        """
        return self._appearance

    @appearance.setter
    def appearance(self, appearance):
        """Sets the appearance of this PartsBatchUpdatePartMetadataBodyParts.


        :param appearance: The appearance of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :type: PartsBatchUpdatePartMetadataBodyAppearance
        """

        self._appearance = appearance

    @property
    def project(self):
        """Gets the project of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501

        Part project  # noqa: E501

        :return: The project of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this PartsBatchUpdatePartMetadataBodyParts.

        Part project  # noqa: E501

        :param project: The project of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def title1(self):
        """Gets the title1 of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501

        Part title 1  # noqa: E501

        :return: The title1 of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :rtype: str
        """
        return self._title1

    @title1.setter
    def title1(self, title1):
        """Sets the title1 of this PartsBatchUpdatePartMetadataBodyParts.

        Part title 1  # noqa: E501

        :param title1: The title1 of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :type: str
        """

        self._title1 = title1

    @property
    def title2(self):
        """Gets the title2 of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501

        Part title 2  # noqa: E501

        :return: The title2 of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :rtype: str
        """
        return self._title2

    @title2.setter
    def title2(self, title2):
        """Sets the title2 of this PartsBatchUpdatePartMetadataBodyParts.

        Part title 2  # noqa: E501

        :param title2: The title2 of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :type: str
        """

        self._title2 = title2

    @property
    def title3(self):
        """Gets the title3 of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501

        Part title 3  # noqa: E501

        :return: The title3 of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :rtype: str
        """
        return self._title3

    @title3.setter
    def title3(self, title3):
        """Sets the title3 of this PartsBatchUpdatePartMetadataBodyParts.

        Part title 3  # noqa: E501

        :param title3: The title3 of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :type: str
        """

        self._title3 = title3

    @property
    def custom_properties(self):
        """Gets the custom_properties of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501

        Custom properties  # noqa: E501

        :return: The custom_properties of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :rtype: list[PartsUpdatePartMetadataBodyCustomProperties]
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this PartsBatchUpdatePartMetadataBodyParts.

        Custom properties  # noqa: E501

        :param custom_properties: The custom_properties of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :type: list[PartsUpdatePartMetadataBodyCustomProperties]
        """

        self._custom_properties = custom_properties

    @property
    def product_line(self):
        """Gets the product_line of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501

        Part product line  # noqa: E501

        :return: The product_line of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :rtype: str
        """
        return self._product_line

    @product_line.setter
    def product_line(self, product_line):
        """Sets the product_line of this PartsBatchUpdatePartMetadataBodyParts.

        Part product line  # noqa: E501

        :param product_line: The product_line of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :type: str
        """

        self._product_line = product_line

    @property
    def part_number(self):
        """Gets the part_number of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501

        Part number  # noqa: E501

        :return: The part_number of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this PartsBatchUpdatePartMetadataBodyParts.

        Part number  # noqa: E501

        :param part_number: The part_number of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :type: str
        """

        self._part_number = part_number

    @property
    def configuration(self):
        """Gets the configuration of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501

        Configuration in which to apply updates  # noqa: E501

        :return: The configuration of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this PartsBatchUpdatePartMetadataBodyParts.

        Configuration in which to apply updates  # noqa: E501

        :param configuration: The configuration of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :type: str
        """

        self._configuration = configuration

    @property
    def revision(self):
        """Gets the revision of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501

        Part revision  # noqa: E501

        :return: The revision of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this PartsBatchUpdatePartMetadataBodyParts.

        Part revision  # noqa: E501

        :param revision: The revision of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def element_id(self):
        """Gets the element_id of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501

        The element ID of the Part Studio containing the part to update  # noqa: E501

        :return: The element_id of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this PartsBatchUpdatePartMetadataBodyParts.

        The element ID of the Part Studio containing the part to update  # noqa: E501

        :param element_id: The element_id of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def name(self):
        """Gets the name of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501

        Part name (Name can only be modified in workspace)  # noqa: E501

        :return: The name of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PartsBatchUpdatePartMetadataBodyParts.

        Part name (Name can only be modified in workspace)  # noqa: E501

        :param name: The name of this PartsBatchUpdatePartMetadataBodyParts.  # noqa: E501
        :type: str
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
        if not isinstance(other, PartsBatchUpdatePartMetadataBodyParts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other