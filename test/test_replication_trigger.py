"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import harbor_client
from harbor_client.model.trigger_settings import TriggerSettings
globals()['TriggerSettings'] = TriggerSettings
from harbor_client.model.replication_trigger import ReplicationTrigger


class TestReplicationTrigger(unittest.TestCase):
    """ReplicationTrigger unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReplicationTrigger(self):
        """Test ReplicationTrigger"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ReplicationTrigger()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
