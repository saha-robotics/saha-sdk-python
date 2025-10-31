import unittest
from unittest.mock import patch
from saha_sdk.client import Robot
from saha_sdk import mapping
from saha_sdk.models import FloorModel, SiteFloorModel, MapModel, MappingModel, ResponseModel


class TestMappingModule(unittest.TestCase):
    """Test cases for mapping module endpoints."""

    def setUp(self):
        """Set up test fixtures."""
        self.client = Robot("https://api.example.com", "test-api-key")

    @patch.object(Robot, 'get')
    def test_get_available_maps(self, mock_get):
        """Test get_available_maps endpoint."""
        mock_response = [
            {"site": "site1", "name": "floor1", "title": "Floor 1", "has_map": True},
            {"site": "site1", "name": "floor2", "title": "Floor 2", "has_map": True}
        ]
        mock_get.return_value = mock_response

        result = mapping.get_available_maps(self.client)

        mock_get.assert_called_once_with("/api/v1/mapping")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], FloorModel)

    @patch.object(Robot, 'get')
    def test_get_default_map(self, mock_get):
        """Test get_default_map endpoint."""
        mock_response = {"site": "site1", "floor": "floor1"}
        mock_get.return_value = mock_response

        result = mapping.get_default_map(self.client)

        mock_get.assert_called_once_with("/api/v1/mapping/default-map")
        self.assertIsInstance(result, SiteFloorModel)

    @patch.object(Robot, 'post')
    def test_set_default_map(self, mock_post):
        """Test set_default_map endpoint."""
        mock_response = {"success": True, "message": "Default map set"}
        mock_post.return_value = mock_response

        site_floor = SiteFloorModel(site="site1", floor="floor1")

        result = mapping.set_default_map(self.client, site_floor)

        mock_post.assert_called_once_with("/api/v1/mapping/default-map", data=site_floor.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'get')
    def test_get_current_map(self, mock_get):
        """Test get_current_map endpoint."""
        mock_response = {
            "site_floor": {"site": "site1", "floor": "floor1"},
            "resolution": 0.05,
            "width": 1024,
            "height": 1024,
            "origin": {"x": 0.0, "y": 0.0, "z": 0.0},
            "map_png_base64": "iVBORw0KGgoAAAANSUhEUg"
        }
        mock_get.return_value = mock_response

        result = mapping.get_current_map(self.client)

        mock_get.assert_called_once_with("/api/v1/mapping/map")
        self.assertIsInstance(result, MapModel)

    @patch.object(Robot, 'get')
    def test_get_selected_map(self, mock_get):
        """Test get_selected_map endpoint."""
        mock_response = {
            "site_floor": {"site": "site1", "floor": "floor1"},
            "resolution": 0.05,
            "width": 1024,
            "height": 1024,
            "origin": {"x": 0.0, "y": 0.0, "z": 0.0},
            "map_png_base64": "iVBORw0KGgoAAAANSUhEUg"
        }
        mock_get.return_value = mock_response

        result = mapping.get_selected_map(self.client, "site1", "floor1")

        mock_get.assert_called_once_with("/api/v1/mapping/site1/floor1")
        self.assertIsInstance(result, MapModel)

    @patch.object(Robot, 'delete')
    def test_delete_selected_map(self, mock_delete):
        """Test delete_selected_map endpoint."""
        mock_response = {"success": True, "message": "Map deleted"}
        mock_delete.return_value = mock_response

        result = mapping.delete_selected_map(self.client, "site1", "floor1")

        mock_delete.assert_called_once_with("/api/v1/mapping/site1/floor1")
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'post')
    def test_start_mapping(self, mock_post):
        """Test start_mapping endpoint."""
        mock_response = {"success": True, "message": "Mapping started"}
        mock_post.return_value = mock_response

        mapping_model = MappingModel(
            site_floor=SiteFloorModel(site="site1", floor="floor1"),
            title="new_map"
        )

        result = mapping.start_mapping(self.client, mapping_model)

        mock_post.assert_called_once_with("/api/v1/mapping/start", data=mapping_model.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'post')
    def test_cancel_mapping(self, mock_post):
        """Test cancel_mapping endpoint."""
        mock_response = {"success": True, "message": "Mapping cancelled"}
        mock_post.return_value = mock_response

        result = mapping.cancel_mapping(self.client)

        mock_post.assert_called_once_with("/api/v1/mapping/cancel")
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'post')
    def test_change_map(self, mock_post):
        """Test change_map endpoint."""
        mock_response = {"success": True, "message": "Map changed"}
        mock_post.return_value = mock_response

        site_floor = SiteFloorModel(site="site1", floor="floor1")

        result = mapping.change_map(self.client, site_floor)

        mock_post.assert_called_once_with("/api/v1/mapping/change", data=site_floor.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'post')
    def test_start_remapping(self, mock_post):
        """Test start_remapping endpoint."""
        mock_response = {"success": True, "message": "Remapping started"}
        mock_post.return_value = mock_response

        site_floor = SiteFloorModel(site="site1", floor="floor1")

        result = mapping.start_remapping(self.client, site_floor)

        mock_post.assert_called_once_with("/api/v1/mapping/remap", data=site_floor.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'post')
    def test_save_map(self, mock_post):
        """Test save_map endpoint."""
        mock_response = {"success": True, "message": "Map saved"}
        mock_post.return_value = mock_response

        result = mapping.save_map(self.client)

        mock_post.assert_called_once_with("/api/v1/mapping/save")
        self.assertIsInstance(result, ResponseModel)


if __name__ == '__main__':
    unittest.main()
