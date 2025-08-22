# saharobotik/navigation.py

from saharobotik.client import SahaRobotikClient


def get_navigation_path(client: SahaRobotikClient):
    """
    Retrieves the robot's current planned navigation path.

    Args:
        client (Robot): API client

    Returns:
        dict: Navigation path information
    """
    return client.get("/api/v1/navigation/path")


def get_navigation_path_stream(client: SahaRobotikClient):
    """
    Enables continuous streaming of the navigation path.

    Args:
        client (Robot): API client

    Returns:
        dict: Real-time navigation path stream data
    """
    return client.get("/api/v1/navigation/path/stream")


def get_current_position(client: SahaRobotikClient):
    """
    Retrieves the robot's current position.

    Args:
        client (Robot): API client

    Returns:
        dict: X, Y coordinates and orientation information
    """
    return client.get("/api/v1/navigation/position")


def get_position_stream(client: SahaRobotikClient):
    """
    Provides the robot's position data as a live stream.

    Args:
        client (Robot): API client

    Returns:
        dict: Real-time position information
    """
    return client.get("/api/v1/navigation/position/stream")


def set_goal_pose(client: SahaRobotikClient, pose: dict):
    """
    Commands the robot to move to a specific X-Y position.

    Args:
        client (Robot): API client
        pose (dict): Target position data (e.g., {"x": 1.0, "y": 2.0, "theta": 0.0})

    Returns:
        dict: Result of the request
    """
    return client.post("/api/v1/navigation/goal/pose", data=pose)


def set_goal_target(client: SahaRobotikClient, target_uid: str):
    """
    Directs the robot to a predefined target using its UID.

    Args:
        client (Robot): API client
        target_uid (str): UID of the target

    Returns:
        dict: Result of the request
    """
    return client.post("/api/v1/navigation/goal/target", data={"target_uid": target_uid})

def get_emergency_stop_status(client: SahaRobotikClient):
    """
    Checks whether the robot is in emergency stop state.

    Args:
        client (Robot): API client

    Returns:
        dict: Emergency stop status
    """
    return client.get("/api/v1/navigation/stop")


def stop_robot(client: SahaRobotikClient):
    """
    Sends an emergency stop command to the robot.

    Args:
        client (Robot): API client

    Returns:
        dict: Result of the stop command
    """
    return client.post("/api/v1/navigation/stop")


def send_safe_velocity(client: SahaRobotikClient, vel: dict):
    """
    Sends a safety-controlled velocity command to the robot.

    Args:
        client (Robot): API client
        vel (dict): Velocity data, e.g., {"x": 0.5, "y": 0.0, "theta": 0.0}

    Returns:
        dict: Result data
    """
    return client.post("/api/v1/navigation/vel/safe", data=vel)


def send_velocity(client: SahaRobotikClient, vel: dict):
    """
    Sends a direct velocity command to the robot (without safety control).

    Args:
        client (Robot): API client
        vel (dict): Velocity data

    Returns:
        dict: Result data
    """
    return client.post("/api/v1/navigation/vel", data=vel)


def start_localization(client: SahaRobotikClient):
    """
    Starts the process to re-localize the robot's position.

    Args:
        client (Robot): API client

    Returns:
        dict: Result of the localization start request
    """
    return client.post("/api/v1/navigation/localization")
