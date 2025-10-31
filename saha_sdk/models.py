from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class RobotStatus(BaseModel):
    is_charging: bool = Field(False, description="Indicates whether the robot is currently charging.", example=False)
    battery_percent: float = Field(100.0, description="Battery percentage of the robot.", example=100.0)
    is_estopped: bool = Field(False, description="Indicates whether the robot is in an emergency stop state.", example=False)
    current_state: str = Field("", description="Current state of the robot.", example="READY_FOR_MISSION")
    out_of_service: bool = Field(False, description="Indicates whether the robot is out of service.", example=False)

class CameraStatus(BaseModel):
    name: str = Field("", description="Name of the camera sensor.", example="front_camera")
    is_working: bool = Field(True, description="Indicates whether the camera sensor is working properly.", example=True)
    state: str = Field("WORKING", description="Current state of the camera sensor.", example="WORKING")
    error: str = Field("", description="Error message if the camera sensor is not working properly.", example="No error")

class SiteFloorModel(BaseModel):
    site: str = Field("", description="The site where the target is located.", example="site")
    floor: str = Field("", description="The floor where the target is located.", example="floor")

class TargetModel(BaseModel):
    name: str = Field(..., min_length=1, description="The name of the target.")
    uid: str = Field(..., min_length=1, description="The unique identifier of the target.")
    site_floor: SiteFloorModel = Field(..., description="The site and floor of the target.")
    eg: str = Field("", description="The entry point of the target.", example="eg_name")
    eg_dir: str = Field("", description="The direction of the entry point.", example="eg_direction")
    px: Optional[float] = Field(0.0, description="The x coordinate of the target in meters.", example=0.0)
    py: Optional[float] = Field(0.0, description="The y coordinate of the target in meters.", example=0.0)
    yaw_deg: Optional[float] = Field(0.0, description="The yaw angle of the target in degrees.", example=0.0)
    tol: float = Field(0.5, description="The tolerance for reaching the target in meters.", example=0.5)
    type: str = Field("default", description="The type of the target('default','charge','waiting','filling','delivery','target','unloading','table','escape','tag').", example="default")
    label: Optional[str] = Field("{}", description="Label of the target.")
    cid: str = Field("", description="The unique identifier of the target, if any.", example="")

class CruiseModel(BaseModel):
    name: str = Field(..., min_length=1, description="The name of the cruise.", example="Cruise 1")
    waypoints: List[TargetModel] = Field(..., description="List of waypoints in the cruise.", example=[{"cid": "", "eg": "", "eg_dir": "", "label": "{}", "name": "Waypoint 1", "px": 0.0, "py": 0.0, "site_floor": {"floor": "floor", "site": "site"}, "tol": 0.5, "type": "default='default'", "uid": "site_floor_target-1", "yaw_deg": 0.0}, {"cid": "", "eg": "", "eg_dir": "", "label": "{}", "name": "Waypoint 2", "px": 0.0, "py": 0.0, "site_floor": {"floor": "floor", "site": "site"}, "tol": 0.5, "type": "default='default'", "uid": "site_floor_target-2", "yaw_deg": 0.0}])
    site_floor: SiteFloorModel = Field(..., description="The site and floor of the cruise.", example={"floor": "floor", "site": "site"})

class CruiseControlRequestModel(BaseModel):
    cruise_cmd: str = Field(..., description="The command to control the cruise (e.g., 'CMD_START, CMD_STOP).", example="CMD_START")
    cruise_route: str = Field("", description="The name of the cruise route to be controlled. If empty uses default route.", example="route_1")
    number_of_rounds: int = Field(1, description="The number of rounds to perform in the cruise.", example=1)

class CruiseRequestModel(BaseModel):
    name: str = Field(..., min_length=1, description="The name of the cruise.", example="Cruise 1")
    waypoints: List[str] = Field(..., description="List of waypoint UIDs in the cruise.", example=["site_floor_target-1", "site_floor_target-2"])
    site: str = Field(..., min_length=1, description="The site where the cruise is located.", example="site")
    floor: str = Field(..., min_length=1, description="The floor where the cruise is located.", example="floor")

class FloorModel(BaseModel):
    site: str = Field("", min_length=1)
    name: str = Field("", min_length=1)
    title: str = Field("", min_length=1)
    elev_groups_default: Optional[str] = Field("")
    elev_groups: Optional[str] = Field("[]")
    has_map: bool = Field(False)

class GoalTargetModel(BaseModel):
    target_uid: str = Field("", description="The unique identifier of the target to navigate to.", example="site_floor_target-1")

class ValidationError(BaseModel):
    loc: List[Any] = Field(...)
    msg: str = Field(...)
    type: str = Field(...)

class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = None

class InternetStatus(BaseModel):
    state: str = Field("DISCONNECTED", description="Current state of the internet connection.", example="DISCONNECTED")
    error: str = Field("", description="Error message if the internet connection is not working properly.", example="No error")
    wifi_enabled: bool = Field(False, description="Indicates whether Wi-Fi is enabled on the robot.", example=False)
    wifi_connected: bool = Field(False, description="Indicates whether the robot is connected to a Wi-Fi network.", example=False)
    wifi_ssid: str = Field("", description="SSID of the connected Wi-Fi network.", example="MyRobotWiFi")
    wifi_ip_addr: str = Field("", description="IP address of the robot on the Wi-Fi network.", example="")
    wifi_mac_addr: str = Field("", description="MAC address of the robot's Wi-Fi interface.", example="00:11:22:33:44:55")
    mobile_enabled: bool = Field(False, description="Indicates whether mobile data is enabled on the robot.", example=False)
    mobile_connected: bool = Field(False, description="Indicates whether the robot is connected to a mobile network.", example=False)

class LayerModel(BaseModel):
    enable: bool = Field(..., description="Indicates whether the layer is enabled or not.")
    type: str = Field(..., description="The type of the layer ('elev', 'buzzer', 'led', 'speed','speech', 'tts', 'slope', 'door', 'map_switch', 'fleet', custom, 'camera', 'uwb', 'directional', 'elev_group').", example="elev")
    options: Dict[str, Any] = Field({}, description="Additional arguments for the layer, such as 'escapes'.")

class Vector3(BaseModel):
    x: float = Field(0.0, description="X coordinate in meters.", example=0.0)
    y: float = Field(0.0, description="Y coordinate in meters.", example=0.0)
    z: float = Field(0.0, description="Z coordinate in meters.", example=0.0)

class LayersModel(BaseModel):
    id: int = Field(..., description="The identifier of the layer.", example=1)
    uid: str = Field(..., description="The unique identifier of the layer.", example="site_floor_layer-1")
    site_floor: SiteFloorModel = Field(..., description="The site and floor of the layer.", example={"floor": "floor", "site": "site"})
    points: List[Vector3] = Field(..., description="List of points defining the layer area.", example=[{"x": 0.0, "y": 0.0, "z": 0.0}, {"x": 1.0, "y": 1.0, "z": 0.0}])
    layers: List[LayerModel] = Field(..., description="List of layers associated with the layer model.", example=[{"enable": True, "options": {"escapes": ["site_floor_target-1", "site_floor_target-2"]}, "type": "elev"}, {"enable": False, "options": {}, "type": "buzzer"}])

class LidarStatus(BaseModel):
    name: str = Field("", description="Name of the lidar sensor.", example="main_lidar")
    is_working: bool = Field(True, description="Indicates whether the lidar sensor is working properly.", example=True)
    state: str = Field("WORKING", description="Current state of the lidar sensor.", example="WORKING")
    error: str = Field("", description="Error message if the lidar sensor is not working properly.", example="No error")

class MapModel(BaseModel):
    site_floor: Optional[SiteFloorModel] = Field(None, description="The site and floor of the map.", example={"floor": "floor", "site": "site"})
    resolution: float = Field(..., description="The resolution of the map in meters per pixel.", example=0.05)
    width: int = Field(..., description="The width of the map in pixels.", example=1024)
    height: int = Field(..., description="The height of the map in pixels.", example=1024)
    origin: Optional[Vector3] = Field(None, description="The origin of the map in the robot's coordinate system.", example={"x": 0.0, "y": 0.0, "z": 0.0})
    map_png_base64: str = Field(..., min_length=1, description="Base64 encoded PNG image of the map.", example="iVBORw0KGgoAAAANSUhEUgAA...")

class MappingModel(BaseModel):
    site_floor: Optional[SiteFloorModel] = Field(None, description="The site and floor of the mapping.")
    title: str = Field("", min_length=1, description="The title of the mapping.", example="site_floor")
    has_map: bool = Field(False)

class Position(BaseModel):
    x: float = Field(0.0, description="X coordinate in meters.", example=0.0)
    y: float = Field(0.0, description="Y coordinate in meters.", example=0.0)
    theta: float = Field(0.0, description="Orientation in radians.", example=0.0)

class PathModel(BaseModel):
    site: str = Field(..., description="The site where the path is located.", example="site")
    floor: str = Field(..., description="The floor where the path is located.", example="floor")
    points: List[Position] = Field(..., description="List of points defining the path.", example=[{"theta": 0.0, "x": 0.0, "y": 0.0}, {"theta": 1.57, "x": 1.0, "y": 1.0}])

class ResponseModel(BaseModel):
    status_code: int = Field(200, description="HTTP status code of the response.", example=200)
    success: bool = Field(True, description="Indicates whether the operation was successful.", example=True)
    message: str = Field("", description="A message providing additional information about the operation.", example="Operation successful")
    data: Optional[Dict[str, Any]] = Field(None, description="Optional data returned by the operation.", example={"key": "value"})
    error: Optional[Dict[str, Any]] = Field(None, description="Optional error information if the operation failed.", example={"code": "ERROR_CODE", "message": "An error occurred"})

class RobotHardwareStatus(BaseModel):
    lidars: List[LidarStatus] = Field(..., description="List of lidar sensors and their statuses.")
    cameras: List[CameraStatus] = Field(..., description="List of camera sensors and their statuses.")
    internet_status: InternetStatus = Field(..., description="Internet connection status of the robot.")

class RobotInfoModel(BaseModel):
    robot_uid: str = Field("", description="The unique identifier of the robot.", example="robot-1")
    project_id: str = Field("", description="The project ID of the robot.", example="project-1")
    site_floor: SiteFloorModel = Field(..., description="The site and floor of the robot.")

class RobotModeModel(BaseModel):
    mode: str = Field("", description="The mode of the robot.", example="normal")

class RobotModes(BaseModel):
    avaible_modes: List[str] = Field(..., description="List of available modes for the robot.", example=["elev"])
    current_modes: List[str] = Field(..., description="List of current modes of the robot.", example=[""])

class RobotProfileModel(BaseModel):
    profile: str = Field("", description="The profile of the robot.", example="normal")

class RobotProfiles(BaseModel):
    avaible_environment_profiles: List[str] = Field(..., description="List of available environment profiles for the robot.", example=["Mall", "Restaurant"])
    avaible_behavior_profiles: List[str] = Field(..., description="List of available behavior profiles for the robot.", example=["Nova", "Default"])
    avaible_speed_profiles: List[str] = Field(..., description="List of available speed profiles for the robot.", example=["slow", "normal", "fast", "faster", "fastest"])
    current_environment_profile: str = Field("indoor", description="The current environment profile of the robot.", example="Restaurant")
    current_behavior_profile: str = Field("normal", description="The current behavior profile of the robot.", example="Nova")
    current_speed_profile: str = Field("medium", description="The current speed profile of the robot.", example="Faster")

class RobotRouteModel(BaseModel):
    route: str = Field("", description="The name of the route to be set for the robot.", example="route_1")

class TwistModel(BaseModel):
    vel_x: float = Field(0.0, description="Linear velocity in the x direction in meters per second.", example=0.0)
    vel_z: float = Field(0.0, description="Angular velocity around the z axis in radians per second.", example=0.0)

class RobotState(BaseModel):
    position: Position = Field(..., description="Current position of the robot in the environment.")
    twist: TwistModel = Field(..., description="Current velocity of the robot in the environment.")

class RobotStopModel(BaseModel):
    stop: bool = Field(False, description="Indicates whether the robot should stop or not.", example=True)

class SpeechModel(BaseModel):
    lang: str = Field(..., description="The language of the text to be spoken by the robot.(e.g., 'tr', 'en').", example="tr")
    text: str = Field(..., description="The text to be spoken by the robot.", example="Hello world")

class TargetRequestModel(BaseModel):
    name: str = Field(..., min_length=1, description="The name of the target.")
    site: str = Field(..., min_length=1, description="The site where the target is located.")
    floor: str = Field(..., min_length=1, description="The floor where the target is located.")
    eg: str = Field(..., description="The entry point of the target.")
    eg_dir: str = Field(..., description="The direction of the entry point.")
    use_current_position: bool = Field(False, description="If True, the current position of the robot will be used as the target position.")
    px: float = Field(0.0, description="The x coordinate of the target in meters.", example=0.0)
    py: float = Field(0.0, description="The y coordinate of the target in meters.", example=0.0)
    yaw_deg: float = Field(0.0, description="The yaw angle of the target in degrees.", example=0.0)
    tol: float = Field(0.5, description="The tolerance for reaching the target in meters.", example=0.5)
    type: str = Field("target", description="The type of the target (default, charge, waiting, filling, delivery, target, unloading, table, escape, tag).", example="target")
    label: Optional[str] = Field("{}", description="Label of the target.")
    cid: str = Field("", description="The unique identifier of the target, if any.", example="")

class TaskModel(BaseModel):
    id: int = Field(..., description="The unique identifier of the task.", example=1)
    uid: int = Field(..., description="The unique identifier of the task, same as id.", example=1)
    site: str = Field(..., description="The site where the task is being performed.", example="site")
    floor: str = Field(..., description="The floor where the task is being performed.", example="floor")
    task_type: str = Field(..., description="The type of the task (e.g., 'TABLE_SERVICE', 'DISH', 'CELEBRATING').", example="TABLE_SERVICE")
    task_index: int = Field(0, description="The index of the task in the task list, if applicable.", example=0)
    success: bool = Field(..., description="Indicates whether the task was successfully started.", example=True)
    completed: bool = Field(..., description="Indicates whether the task was completed successfully.", example=True)
    message: str = Field(..., description="A message providing additional information about the task status.", example="Task started successfully")
    target: TargetModel = Field(..., description="The target to which the robot is navigating.", example={"cid": "", "eg": "", "eg_dir": "", "label": "{}", "name": "Target 1", "px": 0.0, "py": 0.0, "site_floor": {"floor": "floor", "site": "site"}, "tol": 0.5, "type": "default='default'", "uid": "site_floor_target-1", "yaw_deg": 0.0})
    create_time: float = Field(..., description="The timestamp when the task was created.", example=1633036800.0)
    celebrating_name: str = Field("", description="The name of the person to be celebrated, if applicable.", example="John Doe")
    payload: List[bool] = Field(..., description="Which tray or payload is used for the task, if any.", example=[False, False, False, False])

class TaskRequestModel(BaseModel):
    timeout: int = Field(0, description="Timeout in waiting for task start, in seconds.", example=30)
    type: str = Field(..., description="The type of the task (e.g., 'TABLE_SERVICE', 'DISH', 'CELEBRATING').", example="TABLE_SERVICE")
    activate: bool = Field(..., description="Indicates whether the task should be activated or deactivated.", example=True)
    task_index: int = Field(0, description="The index of the task in the task list, if applicable.", example=0)
    target_uid: str = Field(..., min_length=1, description="The unique identifier of the target to which the task is assigned.", example="site_floor_target-1")
    payload: List[bool] = Field(..., description="List of payloads to be used for the task, if any.", example=[False, False, False, False])
    celebrating_name: str = Field("", description="The name of the person to be celebrated, if applicable.", example="John Doe")