from .client import Robot
from .models import RobotStatus, RobotHardwareStatus, RobotInfoModel

def get_robot_status(client: Robot) -> RobotStatus:
    """
    Retrieves the robot's general status information.

    This includes overall system health such as operational state, active task status, current navigation data, and error conditions.

    Args:
        client (Robot): API client

    Returns:
        RobotStatus: General robot status
    """
    response = client.get("/api/v1/status")
    return RobotStatus(**response)

def get_hardware_status(client: Robot) -> RobotHardwareStatus:
    """
    Retrieves the health and connection status of the robot's hardware components.

    This includes battery level, motors, sensors, LIDAR, camera, and other hardware connectivity and functionality status.

    Args:
        client (Robot): API client

    Returns:
        RobotHardwareStatus: Hardware status information
    """
    response = client.get("/api/v1/status/hardware")
    return RobotHardwareStatus(**response)

def get_robot_info(client: Robot) -> RobotInfoModel:
    """
    Retrieves the information of the robot including robot ID, name, model, software version, hardware version, site, floor, and current mission details.

    Args:
        client (Robot): API client

    Returns:
        RobotInfoModel: Robot information
    """
    response = client.get("/api/v1/status/info")
    return RobotInfoModel(**response)