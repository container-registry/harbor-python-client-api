# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import harbor_client
from harbor_client.api.scanner_api import ScannerApi  # noqa: E501
from harbor_client.rest import ApiException


class TestScannerApi(unittest.TestCase):
    """ScannerApi unit test stubs"""

    def setUp(self):
        self.api = api.scanner_api.ScannerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_scanner(self):
        """Test case for create_scanner

        Create a scanner registration  # noqa: E501
        """
        pass

    def test_delete_scanner(self):
        """Test case for delete_scanner

        Delete a scanner registration  # noqa: E501
        """
        pass

    def test_get_scanner(self):
        """Test case for get_scanner

        Get a scanner registration details  # noqa: E501
        """
        pass

    def test_get_scanner_metadata(self):
        """Test case for get_scanner_metadata

        Get the metadata of the specified scanner registration  # noqa: E501
        """
        pass

    def test_list_scanners(self):
        """Test case for list_scanners

        List scanner registrations  # noqa: E501
        """
        pass

    def test_ping_scanner(self):
        """Test case for ping_scanner

        Tests scanner registration settings  # noqa: E501
        """
        pass

    def test_set_scanner_as_default(self):
        """Test case for set_scanner_as_default

        Set system default scanner registration  # noqa: E501
        """
        pass

    def test_update_scanner(self):
        """Test case for update_scanner

        Update a scanner registration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
