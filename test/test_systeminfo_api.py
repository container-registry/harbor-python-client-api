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
from harbor_client.api.systeminfo_api import SysteminfoApi  # noqa: E501
from harbor_client.rest import ApiException


class TestSysteminfoApi(unittest.TestCase):
    """SysteminfoApi unit test stubs"""

    def setUp(self):
        self.api = api.systeminfo_api.SysteminfoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_cert(self):
        """Test case for get_cert

        Get default root certificate.  # noqa: E501
        """
        pass

    def test_get_system_info(self):
        """Test case for get_system_info

        Get general system info  # noqa: E501
        """
        pass

    def test_get_volumes(self):
        """Test case for get_volumes

        Get system volume info (total/free size).  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
