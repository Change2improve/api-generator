# coding: utf-8

"""
    Onshape API

    Onshape API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: ekeller@onshape.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.blob_elements_api import BlobElementsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBlobElementsApi(unittest.TestCase):
    """BlobElementsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.blob_elements_api.BlobElementsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_translation_blob_elements(self):
        """Test case for create_translation_blob_elements

        Create Translation  # noqa: E501
        """
        pass

    def test_download_file_from_element_blob_elements(self):
        """Test case for download_file_from_element_blob_elements

        Download File From Blob Element  # noqa: E501
        """
        pass

    def test_get_translation_formats_blob_elements(self):
        """Test case for get_translation_formats_blob_elements

        Get Translation Formats  # noqa: E501
        """
        pass

    def test_upload_file_create_element_blob_elements(self):
        """Test case for upload_file_create_element_blob_elements

        Upload File to New Blob Element  # noqa: E501
        """
        pass

    def test_upload_file_update_element_blob_elements(self):
        """Test case for upload_file_update_element_blob_elements

        Update Blob Element  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()