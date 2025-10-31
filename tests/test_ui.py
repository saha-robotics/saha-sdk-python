import unittest
from unittest.mock import patch
from saha_sdk.client import Robot
from saha_sdk import ui
from saha_sdk.models import SpeechModel, ResponseModel


class TestUIModule(unittest.TestCase):
    """Test cases for ui module endpoints."""

    def setUp(self):
        """Set up test fixtures."""
        self.client = Robot("https://api.example.com", "test-api-key")

    @patch.object(Robot, 'post')
    def test_speak_text(self, mock_post):
        """Test speak_text endpoint."""
        mock_response = {"success": True, "message": "Speech sent"}
        mock_post.return_value = mock_response

        speech_model = SpeechModel(lang="en", text="Hello, world!")

        result = ui.speak_text(self.client, speech_model)

        mock_post.assert_called_once_with("/api/v1/ui/speech", data=speech_model.model_dump())
        self.assertIsInstance(result, ResponseModel)

    @patch.object(Robot, 'post')
    def test_change_pixel_screen_video(self, mock_post):
        """Test change_pixel_screen_video endpoint."""
        mock_response = {"success": True, "message": "Video changed"}
        mock_post.return_value = mock_response

        video_url = "https://example.com/video.mp4"

        result = ui.change_pixel_screen_video(self.client, video_url)

        mock_post.assert_called_once_with(f"/api/v1/ui/screen/pixel?url={video_url}")
        self.assertIsInstance(result, ResponseModel)


if __name__ == '__main__':
    unittest.main()
