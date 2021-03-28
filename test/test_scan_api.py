"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import harbor-client
from harbor-client.api.scan_api import ScanApi  # noqa: E501


class TestScanApi(unittest.TestCase):
    """ScanApi unit test stubs"""

    def setUp(self):
        self.api = ScanApi()  # noqa: E501

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


if __name__ == '__main__':
    unittest.main()
