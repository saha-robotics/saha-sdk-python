import unittest
from unittest.mock import Mock, patch
from saha_sdk.client import Robot
from saha_sdk import cruise
from saha_sdk.models import RobotRouteModel, CruiseModel, CruiseRequestModel, CruiseControlRequestModel, ResponseModel


class TestCruiseModule(unittest.TestCase):
    """Test cases for cruise module endpoints."""

    def setUp(self):
        """Set up test fixtures."""
        self.client = Robot("https://api.example.com", "test-api-key")

    @patch.object(Robot, 'get')
    def test_get_default_cruise_route(self, mock_get):
        """Test get_default_cruise_route endpoint."""
        mock_response = {
            "route": "route_1"
        }
        mock_get.return_value = mock_response

        result = cruise.get_default_cruise_route(self.client)

        mock_get.assert_called_once_with("/api/v1/config/default-route")
        self.assertIsInstance(result, RobotRouteModel)

    @patch.object(Robot, 'post')
    def test_set_default_cruise_route(self, mock_post):
        """Test set_default_cruise_route endpoint."""
        mock_response = {"success": True, "message": "Route set successfully"}
        mock_post.return_value = mock_response

        route_model = RobotRouteModel(route="route_1")

        result = cruise.set_default_cruise_route(self.client, route_model)

        mock_post.assert_called_once_with("/api/v1/config/default-route", data=route_model.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'get')
    def test_get_all_cruises(self, mock_get):
        """Test get_all_cruises endpoint."""
        mock_response = [
            {
                "name": "cruise1",
                "waypoints": [],
                "site_floor": {"site": "site1", "floor": "floor1"}
            },
            {
                "name": "cruise2",
                "waypoints": [],
                "site_floor": {"site": "site1", "floor": "floor1"}
            }
        ]
        mock_get.return_value = mock_response

        result = cruise.get_all_cruises(self.client)

        mock_get.assert_called_once_with("/api/v1/cruises")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], CruiseModel)

    @patch.object(Robot, 'post')
    def test_add_cruise(self, mock_post):
        """Test add_cruise endpoint."""
        mock_response = {"success": True, "message": "Cruise added"}
        mock_post.return_value = mock_response

        cruise_request = CruiseRequestModel(
            name="test_cruise",
            site="site1",
            floor="floor1",
            waypoints=["target1", "target2"]
        )

        result = cruise.add_cruise(self.client, cruise_request)

        mock_post.assert_called_once_with("/api/v1/cruises", data=cruise_request.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'post')
    def test_start_cruise(self, mock_post):
        """Test start_cruise endpoint."""
        mock_response = {"success": True, "message": "Cruise started"}
        mock_post.return_value = mock_response

        cruise_control = CruiseControlRequestModel(
            cruise_cmd="CMD_START",
            cruise_route="test_cruise"
        )

        result = cruise.start_cruise(self.client, cruise_control)

        mock_post.assert_called_once_with("/api/v1/cruises/control", data=cruise_control.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'get')
    def test_get_cruises_by_site(self, mock_get):
        """Test get_cruises_by_site endpoint."""
        mock_response = [
            {
                "name": "cruise1",
                "waypoints": [],
                "site_floor": {"site": "site1", "floor": "floor1"}
            }
        ]
        mock_get.return_value = mock_response

        result = cruise.get_cruises_by_site(self.client, "site1")

        mock_get.assert_called_once_with("/api/v1/cruises/site1")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], CruiseModel)

    @patch.object(Robot, 'get')
    def test_get_cruises_by_site_and_floor(self, mock_get):
        """Test get_cruises_by_site_and_floor endpoint."""
        mock_response = [
            {
                "name": "cruise1",
                "waypoints": [],
                "site_floor": {"site": "site1", "floor": "floor1"}
            }
        ]
        mock_get.return_value = mock_response

        result = cruise.get_cruises_by_site_and_floor(self.client, "site1", "floor1")

        mock_get.assert_called_once_with("/api/v1/cruises/site1/floor1")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], CruiseModel)

    @patch.object(Robot, 'get')
    def test_get_cruise(self, mock_get):
        """Test get_cruise endpoint."""
        mock_response = {
            "name": "cruise1",
            "waypoints": [],
            "site_floor": {"site": "site1", "floor": "floor1"}
        }
        mock_get.return_value = mock_response

        result = cruise.get_cruise(self.client, "site1", "floor1", "cruise1")

        mock_get.assert_called_once_with("/api/v1/cruises/site1/floor1/cruise1")
        self.assertIsInstance(result, CruiseModel)

    @patch.object(Robot, 'patch')
    def test_update_cruise(self, mock_patch):
        """Test update_cruise endpoint."""
        mock_response = {"success": True, "message": "Cruise updated"}
        mock_patch.return_value = mock_response

        cruise_request = CruiseRequestModel(
            name="cruise1",
            site="site1",
            floor="floor1",
            waypoints=["target1", "target2", "target3"]
        )

        result = cruise.update_cruise(self.client, "site1", "floor1", "cruise1", cruise_request)

        mock_patch.assert_called_once_with("/api/v1/cruises/site1/floor1/cruise1", data=cruise_request.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'delete')
    def test_delete_cruise(self, mock_delete):
        """Test delete_cruise endpoint."""
        mock_response = {"success": True, "message": "Cruise deleted"}
        mock_delete.return_value = mock_response

        result = cruise.delete_cruise(self.client, "site1", "floor1", "cruise1")

        mock_delete.assert_called_once_with("/api/v1/cruises/site1/floor1/cruise1")
        self.assertIsInstance(result, ResponseModel)


if __name__ == '__main__':
    unittest.main()
