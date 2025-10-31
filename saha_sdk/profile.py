from .client import Robot
from .models import RobotProfiles, RobotProfileModel, ResponseModel, RobotModes, RobotModeModel
from typing import List

def get_robot_profiles(client: Robot) -> RobotProfiles:
    """
    Get the current robot profiles including available speed, behavior, and environment profiles.

    Args:
        client (Robot): API client

    Returns:
        RobotProfiles: Robot profiles information
    """
    response = client.get("/api/v1/profile")
    return RobotProfiles(**response)

def change_environment_profile(client: Robot, profile_model: RobotProfileModel) -> ResponseModel:
    """
    Change the environment profile of the robot.

    Args:
        client (Robot): API client
        profile_model (RobotProfileModel): Environment profile to set.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/profile/environment", data=profile_model.dict())
    return ResponseModel(**response)

def change_behavior_profile(client: Robot, profile_model: RobotProfileModel) -> ResponseModel:
    """
    Change the behavior profile of the robot.

    Args:
        client (Robot): API client
        profile_model (RobotProfileModel): Behavior profile to set.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/profile/behavior", data=profile_model.dict())
    return ResponseModel(**response)

def change_speed_profile(client: Robot, profile_model: RobotProfileModel) -> ResponseModel:
    """
    Change the speed profile of the robot.

    Args:
        client (Robot): API client
        profile_model (RobotProfileModel): Speed profile to set.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/profile/speed", data=profile_model.dict())
    return ResponseModel(**response)

def get_robot_modes(client: Robot) -> RobotModes:
    """
    Get the available robot modes.

    Args:
        client (Robot): API client

    Returns:
        RobotModes: Robot modes information
    """
    response = client.get("/api/v1/mode")
    return RobotModes(**response)

def set_robot_mode(client: Robot, mode_model: RobotModeModel) -> ResponseModel:
    """
    Set the robot mode.

    Args:
        client (Robot): API client
        mode_model (RobotModeModel): Robot mode to set.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/mode", data=mode_model.dict())
    return ResponseModel(**response)

def remove_robot_mode(client: Robot, mode_model: RobotModeModel) -> ResponseModel:
    """
    Remove a robot mode.

    Args:
        client (Robot): API client
        mode_model (RobotModeModel): Robot mode to remove.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.delete(f"/api/v1/mode/{mode_model.mode}", data=mode_model.dict())
    return ResponseModel(**response)