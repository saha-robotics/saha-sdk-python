# Saha SDK

[![PyPI version](https://badge.fury.io/py/saha-sdk.svg)](https://badge.fury.io/py/saha-sdk)

Python SDK for the Saha Robotik REST API.

## Installation

```bash
pip install saha-sdk
```

## Usage

```python
from saha_sdk import Robot
from saha_sdk.status import get_robot_status

# Initialize the client with your API key
robot = Robot(base_url="https://api.saharobotik.com", api_key="YOUR_API_KEY")

# Get the robot status
status = get_robot_status(robot)

print(status)
```

## API

The SDK provides a `Robot` class that gives you access to the Saha Robotik API.

### `Robot(base_url, api_key)`

Creates a new API client.

*   `base_url` (str): The base URL of the Saha Robotik API.
*   `api_key` (str): Your API key.

### API Modules

The SDK is organized into modules that correspond to the API resources.

*   `cruise`: Manage cruise routes.
*   `mapping`: Manage maps.
*   `navigation`: Control robot navigation.
*   `profile`: Manage robot profiles.
*   `status`: Get robot status.
*   `targets`: Manage targets.
*   `task`: Manage tasks.
*   `ui`: Control the robot's user interface.

Each module contains functions for interacting with the corresponding API resource. For example, to get the robot's status, you can use the `get_robot_status` function from the `status` module:

```python
from saha_sdk import Robot
from saha_sdk.status import get_robot_status

robot = Robot(base_url="https://api.saharobotik.com", api_key="YOUR_API_KEY")

status = get_robot_status(robot)
```

### Error Handling

The SDK raises exceptions for API errors. All exceptions are subclasses of `SahaRobotikAPIError`.

*   `BadRequestError`: For 400 and 422 errors.
*   `UnauthorizedError`: For 401 and 403 errors.
*   `NotFoundError`: For 404 errors.
*   `ServerError`: For 5xx errors.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
