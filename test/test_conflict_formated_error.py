"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import harbor_client
from harbor_client.model.chart_api_error import ChartAPIError
globals()['ChartAPIError'] = ChartAPIError
from harbor_client.model.conflict_formated_error import ConflictFormatedError


class TestConflictFormatedError(unittest.TestCase):
    """ConflictFormatedError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConflictFormatedError(self):
        """Test ConflictFormatedError"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ConflictFormatedError()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
