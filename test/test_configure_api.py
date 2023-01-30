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
from harbor_client.api.configure_api import ConfigureApi  # noqa: E501
from harbor_client.rest import ApiException


class TestConfigureApi(unittest.TestCase):
    """ConfigureApi unit test stubs"""

    def setUp(self):
        self.api = api.configure_api.ConfigureApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_configurations(self):
        """Test case for get_configurations

        Get system configurations.  # noqa: E501
        """
        pass

    def test_get_internalconfig(self):
        """Test case for get_internalconfig

        Get internal configurations.  # noqa: E501
        """
        pass

    def test_update_configurations(self):
        """Test case for update_configurations

        Modify system configurations.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
