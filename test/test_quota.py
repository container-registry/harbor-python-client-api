"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import harbor_client
from harbor_client.model.quota_ref_object import QuotaRefObject
from harbor_client.model.resource_list import ResourceList
globals()['QuotaRefObject'] = QuotaRefObject
globals()['ResourceList'] = ResourceList
from harbor_client.model.quota import Quota


class TestQuota(unittest.TestCase):
    """Quota unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testQuota(self):
        """Test Quota"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Quota()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
