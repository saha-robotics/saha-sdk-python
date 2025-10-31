import unittest
from unittest.mock import patch
from saha_sdk.client import Robot
from saha_sdk import status
from saha_sdk.models import RobotStatus, RobotHardwareStatus, RobotInfoModel


class TestStatusModule(unittest.TestCase):
    """Test cases for status module endpoints."""

    def setUp(self):
        """Set up test fixtures."""
        self.client = Robot("https://api.example.com", "test-api-key")

    @patch.object(Robot, 'get')
    def test_get_robot_status(self, mock_get):
        """Test get_robot_status endpoint."""
        mock_response = {
            "is_charging": False,
            "battery_percent": 85.0,
            "is_estopped": False,
            "current_state": "READY",
            "out_of_service": False
        }
        mock_get.return_value = mock_response

        result = status.get_robot_status(self.client)

        mock_get.assert_called_once_with("/api/v1/status")
        self.assertIsInstance(result, RobotStatus)

    @patch.object(Robot, 'get')
    def test_get_hardware_status(self, mock_get):
        """Test get_hardware_status endpoint."""
        mock_response = {
            "lidars": [{
                "name": "main_lidar",
                "is_working": True,
                "state": "WORKING",
                "error": ""
            }],
            "cameras": [{
                "name": "front_camera",
                "is_working": True,
                "state": "WORKING",
                "error": ""
            }],
            "internet_status": {
                "state": "CONNECTED",
                "error": "",
                "wifi_enabled": True,
                "wifi_connected": True,
                "wifi_ssid": "TestNetwork",
                "wifi_ip_addr": "192.168.1.100",
                "wifi_mac_addr": "00:11:22:33:44:55",
                "mobile_enabled": False,
                "mobile_connected": False
            }
        }
        mock_get.return_value = mock_response

        result = status.get_hardware_status(self.client)

        mock_get.assert_called_once_with("/api/v1/status/hardware")
        self.assertIsInstance(result, RobotHardwareStatus)

    @patch.object(Robot, 'get')
    def test_get_robot_info(self, mock_get):
        """Test get_robot_info endpoint."""
        mock_response = {
            "robot_uid": "robot123",
            "project_id": "project1",
            "site_floor": {"site": "site1", "floor": "floor1"}
        }
        mock_get.return_value = mock_response

        result = status.get_robot_info(self.client)

        mock_get.assert_called_once_with("/api/v1/status/info")
        self.assertIsInstance(result, RobotInfoModel)


if __name__ == '__main__':
    unittest.main()
