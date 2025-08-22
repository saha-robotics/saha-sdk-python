# saharobotik/profile.py

from .client import SahaRobotikClient

def get_profiles(client: SahaRobotikClient):
    """
    Retrieves the robot's current profile settings (environment, behavior, speed).

    Args:
        client (Robot): API client

    Returns:
        dict: Profile settings
    """
    return client.get("/api/v1/profile")


def set_environment_profile(client: SahaRobotikClient, profile_name: str):
    """
    Changes the robot's environment profile.

    Args:
        client (Robot): API client
        profile_name (str): Name of the environment profile to set

    Returns:
        dict: Result of the operation
    """
    return client.post("/api/v1/profile/environment", data={"profile_name": profile_name})


def set_behavior_profile(client: SahaRobotikClient, profile_name: str):
    """
    Changes the robot's behavior profile.

    Args:
        client (Robot): API client
        profile_name (str): Name of the behavior profile to set

    Returns:
        dict: Result of the operation
    """
    return client.post("/api/v1/profile/behavior", data={"profile_name": profile_name})


def set_speed_profile(client: SahaRobotikClient, profile_name: str):
    """
    Changes the robot's speed profile.

    Args:
        client (Robot): API client
        profile_name (str): Name of the speed profile to set

    Returns:
        dict: Result of the operation
    """
    return client.post("/api/v1/profile/speed", data={"profile_name": profile_name})


def get_modes(client: SahaRobotikClient):
    """
    Lists all operating modes supported by the robot (e.g., patrol, delivery, custom).

    Args:
        client (Robot): API client

    Returns:
        dict: List of available modes
    """
    return client.get("/api/v1/mode")


def set_mode(client: SahaRobotikClient, mode_data: dict):
    """
    Sets the robot's operating mode (e.g., 'auto', 'manual', 'delivery').

    Args:
        client (Robot): API client
        mode_data (dict): Mode data to set (e.g., {"mode": "delivery"})

    Returns:
        dict: Result of the operation
    """
    return client.post("/api/v1/mode", data=mode_data)


def delete_mode(client: SahaRobotikClient, name: str):
    """
    Removes a specific robot mode from the system.

    Args:
        client (Robot): API client
        name (str): Name of the mode to delete

    Returns:
        dict: Result of the deletion operation
    """
    return client.delete(f"/api/v1/mode/{name}")
