import unittest
from unittest.mock import patch
from saha_sdk.client import Robot
from saha_sdk import profile
from saha_sdk.models import RobotProfiles, RobotProfileModel, ResponseModel, RobotModes, RobotModeModel


class TestProfileModule(unittest.TestCase):
    """Test cases for profile module endpoints."""

    def setUp(self):
        """Set up test fixtures."""
        self.client = Robot("https://api.example.com", "test-api-key")

    @patch.object(Robot, 'get')
    def test_get_robot_profiles(self, mock_get):
        """Test get_robot_profiles endpoint."""
        mock_response = {
            "avaible_environment_profiles": ["Mall", "Restaurant"],
            "avaible_behavior_profiles": ["Nova", "Default"],
            "avaible_speed_profiles": ["slow", "normal", "fast"],
            "current_environment_profile": "Mall",
            "current_behavior_profile": "Nova",
            "current_speed_profile": "normal"
        }
        mock_get.return_value = mock_response

        result = profile.get_robot_profiles(self.client)

        mock_get.assert_called_once_with("/api/v1/profile")
        self.assertIsInstance(result, RobotProfiles)

    @patch.object(Robot, 'post')
    def test_change_environment_profile(self, mock_post):
        """Test change_environment_profile endpoint."""
        mock_response = {"success": True, "message": "Environment profile changed"}
        mock_post.return_value = mock_response

        profile_model = RobotProfileModel(profile="indoor")

        result = profile.change_environment_profile(self.client, profile_model)

        mock_post.assert_called_once_with("/api/v1/profile/environment", data=profile_model.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'post')
    def test_change_behavior_profile(self, mock_post):
        """Test change_behavior_profile endpoint."""
        mock_response = {"success": True, "message": "Behavior profile changed"}
        mock_post.return_value = mock_response

        profile_model = RobotProfileModel(profile="cautious")

        result = profile.change_behavior_profile(self.client, profile_model)

        mock_post.assert_called_once_with("/api/v1/profile/behavior", data=profile_model.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'post')
    def test_change_speed_profile(self, mock_post):
        """Test change_speed_profile endpoint."""
        mock_response = {"success": True, "message": "Speed profile changed"}
        mock_post.return_value = mock_response

        profile_model = RobotProfileModel(profile="fast")

        result = profile.change_speed_profile(self.client, profile_model)

        mock_post.assert_called_once_with("/api/v1/profile/speed", data=profile_model.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'get')
    def test_get_robot_modes(self, mock_get):
        """Test get_robot_modes endpoint."""
        mock_response = {
            "avaible_modes": ["patrol", "delivery", "cleaning"],
            "current_modes": ["patrol"]
        }
        mock_get.return_value = mock_response

        result = profile.get_robot_modes(self.client)

        mock_get.assert_called_once_with("/api/v1/mode")
        self.assertIsInstance(result, RobotModes)

    @patch.object(Robot, 'post')
    def test_set_robot_mode(self, mock_post):
        """Test set_robot_mode endpoint."""
        mock_response = {"success": True, "message": "Robot mode set"}
        mock_post.return_value = mock_response

        mode_model = RobotModeModel(mode="delivery")

        result = profile.set_robot_mode(self.client, mode_model)

        mock_post.assert_called_once_with("/api/v1/mode", data=mode_model.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'delete')
    def test_remove_robot_mode(self, mock_delete):
        """Test remove_robot_mode endpoint."""
        mock_response = {"success": True, "message": "Robot mode removed"}
        mock_delete.return_value = mock_response

        mode_model = RobotModeModel(mode="delivery")

        result = profile.remove_robot_mode(self.client, mode_model)

        mock_delete.assert_called_once_with(f"/api/v1/mode/{mode_model.mode}", data=mode_model.model_dump())
        self.assertIsInstance(result, ResponseModel)


if __name__ == '__main__':
    unittest.main()
