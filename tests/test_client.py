import unittest
from unittest.mock import Mock, patch, MagicMock
import requests
from saha_sdk.client import Robot
from saha_sdk.exceptions import (
    SahaRobotikAPIError,
    NotFoundError,
    UnauthorizedError,
    ServerError,
    BadRequestError
)


class TestRobotClient(unittest.TestCase):
    """Test cases for the Robot client class."""

    def setUp(self):
        """Set up test fixtures."""
        self.base_url = "https://api.example.com"
        self.api_key = "test-api-key"
        self.client = Robot(self.base_url, self.api_key)

    def test_init(self):
        """Test Robot client initialization."""
        self.assertEqual(self.client.base_url, self.base_url)
        self.assertEqual(self.client.api_key, self.api_key)
        self.assertEqual(self.client.headers["x-api-key"], self.api_key)
        self.assertEqual(self.client.headers["Content-Type"], "application/json")

    def test_init_with_trailing_slash(self):
        """Test that trailing slash is removed from base_url."""
        client = Robot("https://api.example.com/", self.api_key)
        self.assertEqual(client.base_url, "https://api.example.com")

    def test_full_url(self):
        """Test _full_url method."""
        path = "/api/v1/test"
        expected_url = f"{self.base_url}{path}"
        self.assertEqual(self.client._full_url(path), expected_url)

    @patch('saha_sdk.client.requests.request')
    def test_get_success(self, mock_request):
        """Test successful GET request."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_request.return_value = mock_response

        result = self.client.get("/api/v1/test", params={"key": "value"})

        self.assertEqual(result, {"data": "test"})
        mock_request.assert_called_once_with(
            "GET",
            f"{self.base_url}/api/v1/test",
            headers=self.client.headers,
            params={"key": "value"}
        )

    @patch('saha_sdk.client.requests.request')
    def test_post_success(self, mock_request):
        """Test successful POST request."""
        mock_response = Mock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"success": True}
        mock_request.return_value = mock_response

        result = self.client.post("/api/v1/test", data={"key": "value"})

        self.assertEqual(result, {"success": True})
        mock_request.assert_called_once_with(
            "POST",
            f"{self.base_url}/api/v1/test",
            headers=self.client.headers,
            json={"key": "value"}
        )

    @patch('saha_sdk.client.requests.request')
    def test_patch_success(self, mock_request):
        """Test successful PATCH request."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"updated": True}
        mock_request.return_value = mock_response

        result = self.client.patch("/api/v1/test", data={"key": "value"})

        self.assertEqual(result, {"updated": True})
        mock_request.assert_called_once_with(
            "PATCH",
            f"{self.base_url}/api/v1/test",
            headers=self.client.headers,
            json={"key": "value"}
        )

    @patch('saha_sdk.client.requests.request')
    def test_delete_success(self, mock_request):
        """Test successful DELETE request."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"deleted": True}
        mock_request.return_value = mock_response

        result = self.client.delete("/api/v1/test")

        self.assertEqual(result, {"deleted": True})
        mock_request.assert_called_once_with(
            "DELETE",
            f"{self.base_url}/api/v1/test",
            headers=self.client.headers
        )

    @patch('saha_sdk.client.requests.request')
    def test_response_without_json(self, mock_request):
        """Test handling response without JSON content."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("No JSON")
        mock_response.text = "raw text response"
        mock_request.return_value = mock_response

        result = self.client.get("/api/v1/test")

        self.assertEqual(result, {"raw": "raw text response"})

    @patch('saha_sdk.client.requests.request')
    def test_network_error(self, mock_request):
        """Test network error handling."""
        mock_request.side_effect = requests.RequestException("Connection failed")

        with self.assertRaises(SahaRobotikAPIError) as context:
            self.client.get("/api/v1/test")

        self.assertIn("Network Error", str(context.exception))

    @patch('saha_sdk.client.requests.request')
    def test_400_bad_request_error(self, mock_request):
        """Test 400 Bad Request error."""
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.json.return_value = {"error": {"message": "Bad request"}}
        mock_request.return_value = mock_response

        with self.assertRaises(BadRequestError) as context:
            self.client.get("/api/v1/test")

        self.assertEqual(str(context.exception.message), "Bad request")
        self.assertEqual(context.exception.status_code, 400)

    @patch('saha_sdk.client.requests.request')
    def test_422_validation_error(self, mock_request):
        """Test 422 Validation error."""
        mock_response = Mock()
        mock_response.status_code = 422
        mock_response.json.return_value = {"error": {"message": "Validation failed"}}
        mock_request.return_value = mock_response

        with self.assertRaises(BadRequestError) as context:
            self.client.get("/api/v1/test")

        self.assertEqual(str(context.exception.message), "Validation failed")
        self.assertEqual(context.exception.status_code, 422)

    @patch('saha_sdk.client.requests.request')
    def test_401_unauthorized_error(self, mock_request):
        """Test 401 Unauthorized error."""
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.json.return_value = {"error": {"message": "Unauthorized"}}
        mock_request.return_value = mock_response

        with self.assertRaises(UnauthorizedError) as context:
            self.client.get("/api/v1/test")

        self.assertEqual(str(context.exception.message), "Unauthorized")
        self.assertEqual(context.exception.status_code, 401)

    @patch('saha_sdk.client.requests.request')
    def test_403_forbidden_error(self, mock_request):
        """Test 403 Forbidden error."""
        mock_response = Mock()
        mock_response.status_code = 403
        mock_response.json.return_value = {"error": {"message": "Forbidden"}}
        mock_request.return_value = mock_response

        with self.assertRaises(UnauthorizedError) as context:
            self.client.get("/api/v1/test")

        self.assertEqual(str(context.exception.message), "Forbidden")
        self.assertEqual(context.exception.status_code, 403)

    @patch('saha_sdk.client.requests.request')
    def test_404_not_found_error(self, mock_request):
        """Test 404 Not Found error."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"error": {"message": "Not found"}}
        mock_request.return_value = mock_response

        with self.assertRaises(NotFoundError) as context:
            self.client.get("/api/v1/test")

        self.assertEqual(str(context.exception.message), "Not found")
        self.assertEqual(context.exception.status_code, 404)

    @patch('saha_sdk.client.requests.request')
    def test_500_server_error(self, mock_request):
        """Test 500 Internal Server Error."""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.json.return_value = {"error": {"message": "Internal server error"}}
        mock_request.return_value = mock_response

        with self.assertRaises(ServerError) as context:
            self.client.get("/api/v1/test")

        self.assertEqual(str(context.exception.message), "Internal server error")
        self.assertEqual(context.exception.status_code, 500)

    @patch('saha_sdk.client.requests.request')
    def test_error_without_json_body(self, mock_request):
        """Test error handling when response has no JSON body."""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.json.side_effect = ValueError("No JSON")
        mock_response.text = "Internal Server Error"
        mock_request.return_value = mock_response

        with self.assertRaises(ServerError) as context:
            self.client.get("/api/v1/test")

        self.assertEqual(str(context.exception.message), "Internal Server Error")

    @patch('saha_sdk.client.requests.request')
    def test_unknown_error_code(self, mock_request):
        """Test handling of unknown error status code."""
        mock_response = Mock()
        mock_response.status_code = 418  # I'm a teapot
        mock_response.json.return_value = {"error": {"message": "I'm a teapot"}}
        mock_request.return_value = mock_response

        with self.assertRaises(SahaRobotikAPIError) as context:
            self.client.get("/api/v1/test")

        self.assertEqual(str(context.exception.message), "I'm a teapot")
        self.assertEqual(context.exception.status_code, 418)


if __name__ == '__main__':
    unittest.main()
