import unittest
from unittest.mock import patch
from saha_sdk.client import Robot
from saha_sdk import task
from saha_sdk.models import TaskModel, TaskRequestModel, ResponseModel


class TestTaskModule(unittest.TestCase):
    """Test cases for task module endpoints."""

    def setUp(self):
        """Set up test fixtures."""
        self.client = Robot("https://api.example.com", "test-api-key")

    @patch.object(Robot, 'get')
    def test_get_all_tasks(self, mock_get):
        """Test get_all_tasks endpoint."""
        mock_response = [
            {
                "id": 1,
                "uid": 1,
                "site": "site1",
                "floor": "floor1",
                "task_type": "TABLE_SERVICE",
                "task_index": 0,
                "success": True,
                "completed": False,
                "message": "Task created",
                "target": {
                    "name": "target1",
                    "uid": "site1_floor1_target1",
                    "site_floor": {"site": "site1", "floor": "floor1"},
                    "eg": "",
                    "eg_dir": ""
                },
                "create_time": 1633036800.0,
                "celebrating_name": "",
                "payload": [False, False, False, False]
            }
        ]
        mock_get.return_value = mock_response

        result = task.get_all_tasks(self.client)

        mock_get.assert_called_once_with("/api/v1/tasks")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], TaskModel)

    @patch.object(Robot, 'post')
    def test_create_task(self, mock_post):
        """Test create_task endpoint."""
        mock_response = {"success": True, "message": "Task created"}
        mock_post.return_value = mock_response

        task_request = TaskRequestModel(
            type="TABLE_SERVICE",
            activate=True,
            target_uid="target1",
            payload=[False, False, False, False]
        )

        result = task.create_task(self.client, task_request)

        mock_post.assert_called_once_with("/api/v1/tasks", data=task_request.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'get')
    def test_get_task(self, mock_get):
        """Test get_task endpoint."""
        mock_response = {
            "id": 1,
            "uid": 1,
            "site": "site1",
            "floor": "floor1",
            "task_type": "TABLE_SERVICE",
            "task_index": 0,
            "success": True,
            "completed": False,
            "message": "Task found",
            "target": {
                "name": "target1",
                "uid": "site1_floor1_target1",
                "site_floor": {"site": "site1", "floor": "floor1"},
                "eg": "",
                "eg_dir": ""
            },
            "create_time": 1633036800.0,
            "celebrating_name": "",
            "payload": [False, False, False, False]
        }
        mock_get.return_value = mock_response

        result = task.get_task(self.client, "task123")

        mock_get.assert_called_once_with("/api/v1/tasks/task123")
        self.assertIsInstance(result, TaskModel)

    @patch.object(Robot, 'patch')
    def test_update_task(self, mock_patch):
        """Test update_task endpoint."""
        mock_response = {"success": True, "message": "Task updated"}
        mock_patch.return_value = mock_response

        task_request = TaskRequestModel(
            type="TABLE_SERVICE",
            activate=True,
            target_uid="target1",
            payload=[False, False, False, False]
        )

        result = task.update_task(self.client, "task123", task_request)

        mock_patch.assert_called_once_with("/api/v1/tasks/task123", data=task_request.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'delete')
    def test_delete_task(self, mock_delete):
        """Test delete_task endpoint."""
        mock_response = {"success": True, "message": "Task deleted"}
        mock_delete.return_value = mock_response

        result = task.delete_task(self.client, "task123")

        mock_delete.assert_called_once_with("/api/v1/tasks/task123")
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'post')
    def test_pause_mission(self, mock_post):
        """Test pause_mission endpoint."""
        mock_response = {"success": True, "message": "Mission paused"}
        mock_post.return_value = mock_response

        result = task.pause_mission(self.client)

        mock_post.assert_called_once_with("/api/v1/tasks/pause")
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'post')
    def test_resume_mission(self, mock_post):
        """Test resume_mission endpoint."""
        mock_response = {"success": True, "message": "Mission resumed"}
        mock_post.return_value = mock_response

        result = task.resume_mission(self.client)

        mock_post.assert_called_once_with("/api/v1/tasks/resume")
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'post')
    def test_clear_all_tasks(self, mock_post):
        """Test clear_all_tasks endpoint."""
        mock_response = {"success": True, "message": "All tasks cleared"}
        mock_post.return_value = mock_response

        result = task.clear_all_tasks(self.client)

        mock_post.assert_called_once_with("/api/v1/tasks/clear")
        self.assertIsInstance(result, ResponseModel)


if __name__ == '__main__':
    unittest.main()
