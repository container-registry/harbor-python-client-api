"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import harbor_client
from harbor_client.model.chart_version import ChartVersion
globals()['ChartVersion'] = ChartVersion
from harbor_client.model.search_result import SearchResult


class TestSearchResult(unittest.TestCase):
    """SearchResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearchResult(self):
        """Test SearchResult"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SearchResult()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
