import unittest
from unittest.mock import patch
from saha_sdk.client import Robot
from saha_sdk import layer
from saha_sdk.models import LayersModel


class TestLayerModule(unittest.TestCase):
    """Test cases for layer module endpoints."""

    def setUp(self):
        """Set up test fixtures."""
        self.client = Robot("https://api.example.com", "test-api-key")

    @patch.object(Robot, 'get')
    def test_get_all_layers(self, mock_get):
        """Test get_all_layers endpoint."""
        mock_response = [
            {
                "id": 1,
                "uid": "layer1",
                "site_floor": {"site": "site1", "floor": "floor1"},
                "points": [{"x": 0.0, "y": 0.0, "z": 0.0}],
                "layers": []
            }
        ]
        mock_get.return_value = mock_response

        result = layer.get_all_layers(self.client)

        mock_get.assert_called_once_with("/api/v1/layers")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], LayersModel)

    @patch.object(Robot, 'get')
    def test_get_layers_by_site(self, mock_get):
        """Test get_layers_by_site endpoint."""
        mock_response = [
            {
                "id": 1,
                "uid": "layer1",
                "site_floor": {"site": "site1", "floor": "floor1"},
                "points": [{"x": 0.0, "y": 0.0, "z": 0.0}],
                "layers": []
            }
        ]
        mock_get.return_value = mock_response

        result = layer.get_layers_by_site(self.client, "site1")

        mock_get.assert_called_once_with("/api/v1/layers/site1")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], LayersModel)

    @patch.object(Robot, 'get')
    def test_get_layers_by_site_and_floor(self, mock_get):
        """Test get_layers_by_site_and_floor endpoint."""
        mock_response = [
            {
                "id": 1,
                "uid": "layer1",
                "site_floor": {"site": "site1", "floor": "floor1"},
                "points": [{"x": 0.0, "y": 0.0, "z": 0.0}],
                "layers": []
            }
        ]
        mock_get.return_value = mock_response

        result = layer.get_layers_by_site_and_floor(self.client, "site1", "floor1")

        mock_get.assert_called_once_with("/api/v1/layers/site1/floor1")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], LayersModel)

    @patch.object(Robot, 'get')
    def test_get_layer(self, mock_get):
        """Test get_layer endpoint."""
        mock_response = {
            "id": 1,
            "uid": "layer1",
            "site_floor": {"site": "site1", "floor": "floor1"},
            "points": [{"x": 0.0, "y": 0.0, "z": 0.0}],
            "layers": []
        }
        mock_get.return_value = mock_response

        result = layer.get_layer(self.client, "site1", "floor1", "layer1")

        mock_get.assert_called_once_with("/api/v1/layers/site1/floor1/layer1")
        self.assertIsInstance(result, LayersModel)


if __name__ == '__main__':
    unittest.main()
