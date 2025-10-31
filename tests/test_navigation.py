import unittest
from unittest.mock import Mock, patch
from saha_sdk.client import Robot
from saha_sdk import navigation
from saha_sdk.models import (
    PathModel, Position, RobotState, RobotStopModel,
    SiteFloorModel, ResponseModel, GoalTargetModel, TwistModel
)


class TestNavigationModule(unittest.TestCase):
    """Test cases for navigation module endpoints."""

    def setUp(self):
        """Set up test fixtures."""
        self.client = Robot("https://api.example.com", "test-api-key")

    @patch.object(Robot, 'get')
    def test_get_navigation_path(self, mock_get):
        """Test get_navigation_path endpoint."""
        mock_response = {
            "site": "site1",
            "floor": "floor1",
            "points": [{"x": 1.0, "y": 2.0, "theta": 0.5}]
        }
        mock_get.return_value = mock_response

        result = navigation.get_navigation_path(self.client)

        mock_get.assert_called_once_with("/api/v1/navigation/path")
        self.assertIsInstance(result, PathModel)

    @patch.object(Robot, 'get')
    def test_get_navigation_path_stream(self, mock_get):
        """Test get_navigation_path_stream endpoint."""
        mock_response = {
            "site": "site1",
            "floor": "floor1",
            "points": [{"x": 1.0, "y": 2.0, "theta": 0.5}]
        }
        mock_get.return_value = mock_response

        result = navigation.get_navigation_path_stream(self.client)

        mock_get.assert_called_once_with("/api/v1/navigation/path/stream")
        self.assertIsInstance(result, PathModel)

    @patch.object(Robot, 'get')
    def test_get_current_position(self, mock_get):
        """Test get_current_position endpoint."""
        mock_response = {
            "position": {"x": 1.0, "y": 2.0, "theta": 0.5},
            "twist": {"vel_x": 0.0, "vel_z": 0.0}
        }
        mock_get.return_value = mock_response

        result = navigation.get_current_position(self.client)

        mock_get.assert_called_once_with("/api/v1/navigation/position")
        self.assertIsInstance(result, RobotState)

    @patch.object(Robot, 'get')
    def test_get_position_stream(self, mock_get):
        """Test get_position_stream endpoint."""
        mock_response = {
            "position": {"x": 1.0, "y": 2.0, "theta": 0.5},
            "twist": {"vel_x": 0.0, "vel_z": 0.0}
        }
        mock_get.return_value = mock_response

        result = navigation.get_position_stream(self.client)

        mock_get.assert_called_once_with("/api/v1/navigation/position/stream")
        self.assertIsInstance(result, RobotState)

    @patch.object(Robot, 'post')
    def test_set_goal_pose(self, mock_post):
        """Test set_goal_pose endpoint."""
        mock_response = {"success": True, "message": "Goal set"}
        mock_post.return_value = mock_response

        pose = Position(x=1.0, y=2.0, theta=0.5)

        result = navigation.set_goal_pose(self.client, pose)

        mock_post.assert_called_once_with("/api/v1/navigation/goal/pose", data=pose.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'post')
    def test_set_goal_target(self, mock_post):
        """Test set_goal_target endpoint."""
        mock_response = {"success": True, "message": "Goal set"}
        mock_post.return_value = mock_response

        target_uid = "target123"

        result = navigation.set_goal_target(self.client, target_uid)

        mock_post.assert_called_once_with(
            "/api/v1/navigation/goal/target",
            data=GoalTargetModel(target_uid=target_uid).model_dump()
        )
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'get')
    def test_get_emergency_stop_status(self, mock_get):
        """Test get_emergency_stop_status endpoint."""
        mock_response = {"stop": False}
        mock_get.return_value = mock_response

        result = navigation.get_emergency_stop_status(self.client)

        mock_get.assert_called_once_with("/api/v1/navigation/stop")
        self.assertIsInstance(result, RobotStopModel)

    @patch.object(Robot, 'post')
    def test_set_emergency_stop(self, mock_post):
        """Test set_emergency_stop endpoint."""
        mock_response = {"success": True, "message": "Emergency stop set"}
        mock_post.return_value = mock_response

        stop_model = RobotStopModel(stop=True)

        result = navigation.set_emergency_stop(self.client, stop_model)

        mock_post.assert_called_once_with("/api/v1/navigation/stop", data=stop_model.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'post')
    def test_send_safe_velocity(self, mock_post):
        """Test send_safe_velocity endpoint."""
        mock_response = {"success": True, "message": "Velocity sent"}
        mock_post.return_value = mock_response

        vel = TwistModel(vel_x=0.5, vel_z=0.0)

        result = navigation.send_safe_velocity(self.client, vel)

        mock_post.assert_called_once_with("/api/v1/navigation/vel/safe", data=vel.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'post')
    def test_send_velocity(self, mock_post):
        """Test send_velocity endpoint."""
        mock_response = {"success": True, "message": "Velocity sent"}
        mock_post.return_value = mock_response

        vel = TwistModel(vel_x=0.5, vel_z=0.0)

        result = navigation.send_velocity(self.client, vel)

        mock_post.assert_called_once_with("/api/v1/navigation/vel", data=vel.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'post')
    def test_start_localization(self, mock_post):
        """Test start_localization endpoint."""
        mock_response = {"success": True, "message": "Localization started"}
        mock_post.return_value = mock_response

        site_floor = SiteFloorModel(site="site1", floor="floor1")

        result = navigation.start_localization(self.client, site_floor)

        mock_post.assert_called_once_with("/api/v1/navigation/localization", data=site_floor.model_dump())
        self.assertIsInstance(result, ResponseModel)


if __name__ == '__main__':
    unittest.main()
