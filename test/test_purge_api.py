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
from harbor_client.api.purge_api import PurgeApi  # noqa: E501
from harbor_client.rest import ApiException


class TestPurgeApi(unittest.TestCase):
    """PurgeApi unit test stubs"""

    def setUp(self):
        self.api = api.purge_api.PurgeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_purge_schedule(self):
        """Test case for create_purge_schedule

        Create a purge job schedule.  # noqa: E501
        """
        pass

    def test_get_purge_history(self):
        """Test case for get_purge_history

        Get purge job results.  # noqa: E501
        """
        pass

    def test_get_purge_job(self):
        """Test case for get_purge_job

        Get purge job status.  # noqa: E501
        """
        pass

    def test_get_purge_job_log(self):
        """Test case for get_purge_job_log

        Get purge job log.  # noqa: E501
        """
        pass

    def test_get_purge_schedule(self):
        """Test case for get_purge_schedule

        Get purge's schedule.  # noqa: E501
        """
        pass

    def test_stop_purge(self):
        """Test case for stop_purge

        Stop the specific purge audit log execution  # noqa: E501
        """
        pass

    def test_update_purge_schedule(self):
        """Test case for update_purge_schedule

        Update purge job's schedule.  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
