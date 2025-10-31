import unittest
from unittest.mock import patch
from saha_sdk.client import Robot
from saha_sdk import targets
from saha_sdk.models import TargetModel, TargetRequestModel, ResponseModel


class TestTargetsModule(unittest.TestCase):
    """Test cases for targets module endpoints."""

    def setUp(self):
        """Set up test fixtures."""
        self.client = Robot("https://api.example.com", "test-api-key")

    @patch.object(Robot, 'get')
    def test_get_all_targets(self, mock_get):
        """Test get_all_targets endpoint."""
        mock_response = [
            {
                "name": "target1",
                "uid": "site1_floor1_target1",
                "site_floor": {"site": "site1", "floor": "floor1"},
                "eg": "",
                "eg_dir": "",
                "px": 1.0,
                "py": 2.0,
                "yaw_deg": 0.0
            }
        ]
        mock_get.return_value = mock_response

        result = targets.get_all_targets(self.client)

        mock_get.assert_called_once_with("/api/v1/targets")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], TargetModel)

    @patch.object(Robot, 'post')
    def test_add_target(self, mock_post):
        """Test add_target endpoint."""
        mock_response = {"success": True, "message": "Target added"}
        mock_post.return_value = mock_response

        target_request = TargetRequestModel(
            name="new_target",
            site="site1",
            floor="floor1",
            eg="eg1",
            eg_dir="forward",
            px=1.0,
            py=2.0,
            yaw_deg=0.5
        )

        result = targets.add_target(self.client, target_request)

        mock_post.assert_called_once_with("/api/v1/targets", data=target_request.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'get')
    def test_get_targets_by_site(self, mock_get):
        """Test get_targets_by_site endpoint."""
        mock_response = [
            {
                "name": "target1",
                "uid": "site1_floor1_target1",
                "site_floor": {"site": "site1", "floor": "floor1"},
                "eg": "",
                "eg_dir": "",
                "px": 1.0,
                "py": 2.0,
                "yaw_deg": 0.0
            }
        ]
        mock_get.return_value = mock_response

        result = targets.get_targets_by_site(self.client, "site1")

        mock_get.assert_called_once_with("/api/v1/targets/site1")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], TargetModel)

    @patch.object(Robot, 'get')
    def test_get_targets_by_site_and_floor(self, mock_get):
        """Test get_targets_by_site_and_floor endpoint."""
        mock_response = [
            {
                "name": "target1",
                "uid": "site1_floor1_target1",
                "site_floor": {"site": "site1", "floor": "floor1"},
                "eg": "",
                "eg_dir": "",
                "px": 1.0,
                "py": 2.0,
                "yaw_deg": 0.0
            }
        ]
        mock_get.return_value = mock_response

        result = targets.get_targets_by_site_and_floor(self.client, "site1", "floor1")

        mock_get.assert_called_once_with("/api/v1/targets/site1/floor1")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], TargetModel)

    @patch.object(Robot, 'get')
    def test_get_target(self, mock_get):
        """Test get_target endpoint."""
        mock_response = {
            "name": "target1",
            "uid": "site1_floor1_target1",
            "site_floor": {"site": "site1", "floor": "floor1"},
            "eg": "",
            "eg_dir": "",
            "px": 1.0,
            "py": 2.0,
            "yaw_deg": 0.0
        }
        mock_get.return_value = mock_response

        result = targets.get_target(self.client, "site1", "floor1", "target1")

        mock_get.assert_called_once_with("/api/v1/targets/site1/floor1/target1")
        self.assertIsInstance(result, TargetModel)

    @patch.object(Robot, 'patch')
    def test_update_target(self, mock_patch):
        """Test update_target endpoint."""
        mock_response = {"success": True, "message": "Target updated"}
        mock_patch.return_value = mock_response

        target_request = TargetRequestModel(
            name="target1",
            site="site1",
            floor="floor1",
            eg="eg1",
            eg_dir="forward",
            px=2.0,
            py=3.0,
            yaw_deg=1.0
        )

        result = targets.update_target(self.client, "site1", "floor1", "target1", target_request)

        mock_patch.assert_called_once_with("/api/v1/targets/site1/floor1/target1", data=target_request.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'delete')
    def test_delete_target(self, mock_delete):
        """Test delete_target endpoint."""
        mock_response = {"success": True, "message": "Target deleted"}
        mock_delete.return_value = mock_response

        result = targets.delete_target(self.client, "site1", "floor1", "target1")

        mock_delete.assert_called_once_with("/api/v1/targets/site1/floor1/target1")
        self.assertIsInstance(result, ResponseModel)


if __name__ == '__main__':
    unittest.main()
