# saharobotik/client.py

import requests
from typing import Optional, Dict, Any
from .exceptions import (
    SahaRobotikAPIError,
    NotFoundError,
    UnauthorizedError,
    ServerError,
    BadRequestError
)


class Robot:
    """A client for the Saha Robotik API."""
    def __init__(self, base_url: str, api_key: str):
        """Initializes a new client.

        Args:
            base_url: The base URL of the Saha Robotik API.
            api_key: Your API key.
        """
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }

    def _full_url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Sends a GET request to the API.

        Args:
            path: The path of the API endpoint.
            params: The query parameters.

        Returns:
            The JSON response from the API.
        """
        return self._request("GET", path, params=params)

    def post(self, path: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Sends a POST request to the API.

        Args:
            path: The path of the API endpoint.
            data: The request body.

        Returns:
            The JSON response from the API.
        """
        return self._request("POST", path, json=data)

    def patch(self, path: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Sends a PATCH request to the API.

        Args:
            path: The path of the API endpoint.
            data: The request body.

        Returns:
            The JSON response from the API.
        """
        return self._request("PATCH", path, json=data)

    def delete(self, path: str) -> Dict[str, Any]:
        """Sends a DELETE request to the API.

        Args:
            path: The path of the API endpoint.

        Returns:
            The JSON response from the API.
        """
        return self._request("DELETE", path)

    def _request(self, method: str, path: str, **kwargs) -> Dict[str, Any]:
        url = self._full_url(path)
        try:
            response = requests.request(method, url, headers=self.headers, **kwargs)
        except requests.RequestException as e:
            raise SahaRobotikAPIError(f"Network Error: {str(e)}")

        return self._handle_response(response)

    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        if 200 <= response.status_code < 300:
            try:
                return response.json()
            except ValueError:
                return {"raw": response.text}

        try:
            error_data = response.json()
            error_msg = error_data.get("error", {}).get("message", response.text)
        except ValueError:
            error_msg = response.text

        if response.status_code == 400 or response.status_code == 422:
            raise BadRequestError(error_msg, status_code=response.status_code, response=response)
        elif response.status_code == 401 or response.status_code == 403:
            raise UnauthorizedError(error_msg, status_code=response.status_code, response=response)
        elif response.status_code == 404:
            raise NotFoundError(error_msg, status_code=response.status_code, response=response)
        elif 500 <= response.status_code < 600:
            raise ServerError(error_msg, status_code=response.status_code, response=response)
        else:
            raise SahaRobotikAPIError(error_msg, status_code=response.status_code, response=response)
