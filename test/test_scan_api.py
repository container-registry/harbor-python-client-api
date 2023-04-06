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
from harbor_client.api.scan_api import ScanApi  # noqa: E501
from harbor_client.rest import ApiException


class TestScanApi(unittest.TestCase):
    """ScanApi unit test stubs"""

    def setUp(self):
        self.api = api.scan_api.ScanApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_report_log(self):
        """Test case for get_report_log

        Get the log of the scan report  # noqa: E501
        """
        pass

    def test_scan_artifact(self):
        """Test case for scan_artifact

        Scan the artifact  # noqa: E501
        """
        pass

    def test_stop_scan_artifact(self):
        """Test case for stop_scan_artifact

        Cancelling a scan job for a particular artifact  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
