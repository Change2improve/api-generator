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

from onshape_client.models.release_management_create_release_package_response200_errors import ReleaseManagementCreateReleasePackageResponse200Errors  # noqa: F401,E501
from onshape_client.models.release_management_create_release_package_response200_properties import ReleaseManagementCreateReleasePackageResponse200Properties  # noqa: F401,E501


class ReleaseManagementCreateReleasePackageResponse200Items(object):
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
        'properties': 'list[ReleaseManagementCreateReleasePackageResponse200Properties]',
        'errors': 'list[ReleaseManagementCreateReleasePackageResponse200Errors]',
        'name': 'str',
        'part_id': 'str',
        'href': 'str',
        'elment_type': 'float',
        'children': 'list[object]',
        'version_id': 'str',
        'workspace_id': 'str',
        'document_id': 'str',
        'configuration': 'str',
        'id': 'str',
        'element_id': 'str',
        'view_ref': 'str'
    }

    attribute_map = {
        'properties': 'properties',
        'errors': 'errors',
        'name': 'name',
        'part_id': 'partId',
        'href': 'href',
        'elment_type': 'elmentType',
        'children': 'children',
        'version_id': 'versionId',
        'workspace_id': 'workspaceId',
        'document_id': 'documentId',
        'configuration': 'configuration',
        'id': 'id',
        'element_id': 'elementId',
        'view_ref': 'viewRef'
    }

    def __init__(self, properties=None, errors=None, name=None, part_id=None, href=None, elment_type=None, children=None, version_id=None, workspace_id=None, document_id=None, configuration=None, id=None, element_id=None, view_ref=None):  # noqa: E501
        """ReleaseManagementCreateReleasePackageResponse200Items - a model defined in Swagger"""  # noqa: E501

        self._properties = None
        self._errors = None
        self._name = None
        self._part_id = None
        self._href = None
        self._elment_type = None
        self._children = None
        self._version_id = None
        self._workspace_id = None
        self._document_id = None
        self._configuration = None
        self._id = None
        self._element_id = None
        self._view_ref = None
        self.discriminator = None

        if properties is not None:
            self.properties = properties
        if errors is not None:
            self.errors = errors
        if name is not None:
            self.name = name
        if part_id is not None:
            self.part_id = part_id
        if href is not None:
            self.href = href
        if elment_type is not None:
            self.elment_type = elment_type
        if children is not None:
            self.children = children
        if version_id is not None:
            self.version_id = version_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if document_id is not None:
            self.document_id = document_id
        if configuration is not None:
            self.configuration = configuration
        if id is not None:
            self.id = id
        if element_id is not None:
            self.element_id = element_id
        if view_ref is not None:
            self.view_ref = view_ref

    @property
    def properties(self):
        """Gets the properties of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501

        Properties of the item  # noqa: E501

        :return: The properties of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :rtype: list[ReleaseManagementCreateReleasePackageResponse200Properties]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ReleaseManagementCreateReleasePackageResponse200Items.

        Properties of the item  # noqa: E501

        :param properties: The properties of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :type: list[ReleaseManagementCreateReleasePackageResponse200Properties]
        """

        self._properties = properties

    @property
    def errors(self):
        """Gets the errors of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501

        Errors or warnings if any associated with items.  # noqa: E501

        :return: The errors of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :rtype: list[ReleaseManagementCreateReleasePackageResponse200Errors]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ReleaseManagementCreateReleasePackageResponse200Items.

        Errors or warnings if any associated with items.  # noqa: E501

        :param errors: The errors of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :type: list[ReleaseManagementCreateReleasePackageResponse200Errors]
        """

        self._errors = errors

    @property
    def name(self):
        """Gets the name of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501

        Name of the revisionable object  # noqa: E501

        :return: The name of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReleaseManagementCreateReleasePackageResponse200Items.

        Name of the revisionable object  # noqa: E501

        :param name: The name of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def part_id(self):
        """Gets the part_id of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501

        Deterministic part ID if item is a part  # noqa: E501

        :return: The part_id of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id):
        """Sets the part_id of this ReleaseManagementCreateReleasePackageResponse200Items.

        Deterministic part ID if item is a part  # noqa: E501

        :param part_id: The part_id of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :type: str
        """

        self._part_id = part_id

    @property
    def href(self):
        """Gets the href of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501

        An URI to get complete metadata for the item  # noqa: E501

        :return: The href of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ReleaseManagementCreateReleasePackageResponse200Items.

        An URI to get complete metadata for the item  # noqa: E501

        :param href: The href of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def elment_type(self):
        """Gets the elment_type of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501

        Type of element, which can be 0: Part Studio, 1: Assembly, 2:             Drawing. 4: Blob  # noqa: E501

        :return: The elment_type of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :rtype: float
        """
        return self._elment_type

    @elment_type.setter
    def elment_type(self, elment_type):
        """Sets the elment_type of this ReleaseManagementCreateReleasePackageResponse200Items.

        Type of element, which can be 0: Part Studio, 1: Assembly, 2:             Drawing. 4: Blob  # noqa: E501

        :param elment_type: The elment_type of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :type: float
        """

        self._elment_type = elment_type

    @property
    def children(self):
        """Gets the children of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501

        Dependent child items as determined by Onshape. Assemblies             and Drawings will contain all their references recursively unless they have been explicitly marked as             non revision managed.  # noqa: E501

        :return: The children of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :rtype: list[object]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this ReleaseManagementCreateReleasePackageResponse200Items.

        Dependent child items as determined by Onshape. Assemblies             and Drawings will contain all their references recursively unless they have been explicitly marked as             non revision managed.  # noqa: E501

        :param children: The children of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :type: list[object]
        """

        self._children = children

    @property
    def version_id(self):
        """Gets the version_id of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501

        Version ID of the revisionable object  # noqa: E501

        :return: The version_id of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this ReleaseManagementCreateReleasePackageResponse200Items.

        Version ID of the revisionable object  # noqa: E501

        :param version_id: The version_id of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501

        Workspace ID of the revisionable object  # noqa: E501

        :return: The workspace_id of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ReleaseManagementCreateReleasePackageResponse200Items.

        Workspace ID of the revisionable object  # noqa: E501

        :param workspace_id: The workspace_id of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def document_id(self):
        """Gets the document_id of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501

        Document ID of the revisionable object  # noqa: E501

        :return: The document_id of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this ReleaseManagementCreateReleasePackageResponse200Items.

        Document ID of the revisionable object  # noqa: E501

        :param document_id: The document_id of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def configuration(self):
        """Gets the configuration of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501

        Configuration of the Part studio or Assembly element  # noqa: E501

        :return: The configuration of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this ReleaseManagementCreateReleasePackageResponse200Items.

        Configuration of the Part studio or Assembly element  # noqa: E501

        :param configuration: The configuration of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :type: str
        """

        self._configuration = configuration

    @property
    def id(self):
        """Gets the id of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501

        ID of the item  # noqa: E501

        :return: The id of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReleaseManagementCreateReleasePackageResponse200Items.

        ID of the item  # noqa: E501

        :param id: The id of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def element_id(self):
        """Gets the element_id of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501

        Element ID of the revisionable object  # noqa: E501

        :return: The element_id of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this ReleaseManagementCreateReleasePackageResponse200Items.

        Element ID of the revisionable object  # noqa: E501

        :param element_id: The element_id of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def view_ref(self):
        """Gets the view_ref of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501

        An URI that can be opened in the browser to view the item  # noqa: E501

        :return: The view_ref of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this ReleaseManagementCreateReleasePackageResponse200Items.

        An URI that can be opened in the browser to view the item  # noqa: E501

        :param view_ref: The view_ref of this ReleaseManagementCreateReleasePackageResponse200Items.  # noqa: E501
        :type: str
        """

        self._view_ref = view_ref

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
        if not isinstance(other, ReleaseManagementCreateReleasePackageResponse200Items):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other