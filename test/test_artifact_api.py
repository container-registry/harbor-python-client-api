"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import harbor-client
from harbor-client.api.artifact_api import ArtifactApi  # noqa: E501


class TestArtifactApi(unittest.TestCase):
    """ArtifactApi unit test stubs"""

    def setUp(self):
        self.api = ArtifactApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_label(self):
        """Test case for add_label

        Add label to artifact  # noqa: E501
        """
        pass

    def test_copy_artifact(self):
        """Test case for copy_artifact

        Copy artifact  # noqa: E501
        """
        pass

    def test_create_tag(self):
        """Test case for create_tag

        Create tag  # noqa: E501
        """
        pass

    def test_delete_artifact(self):
        """Test case for delete_artifact

        Delete the specific artifact  # noqa: E501
        """
        pass

    def test_delete_tag(self):
        """Test case for delete_tag

        Delete tag  # noqa: E501
        """
        pass

    def test_get_addition(self):
        """Test case for get_addition

        Get the addition of the specific artifact  # noqa: E501
        """
        pass

    def test_get_artifact(self):
        """Test case for get_artifact

        Get the specific artifact  # noqa: E501
        """
        pass

    def test_list_artifacts(self):
        """Test case for list_artifacts

        List artifacts  # noqa: E501
        """
        pass

    def test_list_tags(self):
        """Test case for list_tags

        List tags  # noqa: E501
        """
        pass

    def test_remove_label(self):
        """Test case for remove_label

        Remove label from artifact  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
