from .client import Robot
from .models import PathModel, Position, RobotState, RobotStopModel, SiteFloorModel, ResponseModel, GoalTargetModel, TwistModel
from typing import Dict, Any

def get_navigation_path(client: Robot) -> PathModel:
    """
    Retrieves the robot's current planned navigation path.

    Args:
        client (Robot): API client

    Returns:
        PathModel: Navigation path information
    """
    response = client.get("/api/v1/navigation/path")
    return PathModel(**response)

def get_navigation_path_stream(client: Robot) -> PathModel:
    """
    Enables continuous streaming of the navigation path.

    Args:
        client (Robot): API client

    Returns:
        PathModel: Real-time navigation path stream data
    """
    response = client.get("/api/v1/navigation/path/stream")
    return PathModel(**response)

def get_current_position(client: Robot) -> RobotState:
    """
    Retrieves the robot's current position.

    Args:
        client (Robot): API client

    Returns:
        RobotState: X, Y coordinates and orientation information
    """
    response = client.get("/api/v1/navigation/position")
    return RobotState(**response)

def get_position_stream(client: Robot) -> RobotState:
    """
    Provides the robot's position data as a live stream.

    Args:
        client (Robot): API client

    Returns:
        RobotState: Real-time position information
    """
    response = client.get("/api/v1/navigation/position/stream")
    return RobotState(**response)

def set_goal_pose(client: Robot, pose: Position) -> ResponseModel:
    """
    Commands the robot to move to a specific X-Y position.

    Args:
        client (Robot): API client
        pose (Position): Target position data (e.g., {"x": 1.0, "y": 2.0, "theta": 0.0})

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/navigation/goal/pose", data=pose.dict())
    return ResponseModel(**response)

def set_goal_target(client: Robot, target_uid: str) -> ResponseModel:
    """
    Directs the robot to a predefined target using its UID.

    Args:
        client (Robot): API client
        target_uid (str): UID of the target

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/navigation/goal/target", data=GoalTargetModel(target_uid=target_uid).dict())
    return ResponseModel(**response)

def get_emergency_stop_status(client: Robot) -> RobotStopModel:
    """
    Checks whether the robot is in emergency stop state.

    Args:
        client (Robot): API client

    Returns:
        RobotStopModel: Emergency stop status
    """
    response = client.get("/api/v1/navigation/stop")
    return RobotStopModel(**response)

def set_emergency_stop(client: Robot, stop_model: RobotStopModel) -> ResponseModel:
    """
    Set the emergency stop status of the robot.

    Args:
        client (Robot): API client
        stop_model (RobotStopModel): Emergency stop status data (e.g., {"stop": True})

    Returns:
        ResponseModel: Result of the stop command
    """
    response = client.post("/api/v1/navigation/stop", data=stop_model.dict())
    return ResponseModel(**response)

def send_safe_velocity(client: Robot, vel: TwistModel) -> ResponseModel:
    """
    Sends a safety-controlled velocity command to the robot.

    Args:
        client (Robot): API client
        vel (TwistModel): Velocity data, e.g., {"vel_x": 0.5, "vel_z": 0.0}

    Returns:
        ResponseModel: Result data
    """
    response = client.post("/api/v1/navigation/vel/safe", data=vel.dict())
    return ResponseModel(**response)

def send_velocity(client: Robot, vel: TwistModel) -> ResponseModel:
    """
    Sends a direct velocity command to the robot (without safety control).

    Args:
        client (Robot): API client
        vel (TwistModel): Velocity data

    Returns:
        ResponseModel: Result data
    """
    response = client.post("/api/v1/navigation/vel", data=vel.dict())
    return ResponseModel(**response)

def start_localization(client: Robot, site_floor: SiteFloorModel) -> ResponseModel:
    """
    Starts the process to re-localize the robot's position.

    Args:
        client (Robot): API client
        site_floor (SiteFloorModel): Site and floor information for localization.

    Returns:
        ResponseModel: Result of the localization start request
    """
    response = client.post("/api/v1/navigation/localization", data=site_floor.dict())
    return ResponseModel(**response)