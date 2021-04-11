"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import harbor_client
from harbor_client.api.ldap_api import LdapApi  # noqa: E501


class TestLdapApi(unittest.TestCase):
    """LdapApi unit test stubs"""

    def setUp(self):
        self.api = LdapApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_import_ldap_user(self):
        """Test case for import_ldap_user

        Import selected available ldap users.  # noqa: E501
        """
        pass

    def test_ping_ldap(self):
        """Test case for ping_ldap

        Ping available ldap service.  # noqa: E501
        """
        pass

    def test_search_ldap_group(self):
        """Test case for search_ldap_group

        Search available ldap groups.  # noqa: E501
        """
        pass

    def test_search_ldap_user(self):
        """Test case for search_ldap_user

        Search available ldap users.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
