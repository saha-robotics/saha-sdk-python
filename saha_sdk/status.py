# saharobotik/status.py

from .client import SahaRobotikClient


def get_robot_status(client: SahaRobotikClient):
    """
    Retrieves the robot's general status information.

    This includes overall system health such as operational state, active task status, current navigation data, and error conditions.

    Args:
        client (Robot): API client

    Returns:
        dict: General robot status
    """
    return client.get("/api/v1/status")


def get_hardware_status(client: SahaRobotikClient):
    """
    Retrieves the health and connection status of the robot's hardware components.

    This includes battery level, motors, sensors, LIDAR, camera, and other hardware connectivity and functionality status.

    Args:
        client (Robot): API client

    Returns:
        dict: Hardware status information
    """
    return client.get("/api/v1/status/hardware")
