from .client import Robot
from .models import FloorModel, SiteFloorModel, MapModel, MappingModel, ResponseModel
from typing import List

def get_available_maps(client: Robot) -> List[FloorModel]:
    """
    Get the list of available maps (floors) for the robot.

    Args:
        client (Robot): API client

    Returns:
        List[FloorModel]: List of available maps
    """
    response = client.get("/api/v1/mapping")
    return [FloorModel(**item) for item in response]

def get_default_map(client: Robot) -> SiteFloorModel:
    """
    Get the default map for the robot.

    Args:
        client (Robot): API client

    Returns:
        SiteFloorModel: Default map information
    """
    response = client.get("/api/v1/mapping/default-map")
    return SiteFloorModel(**response)

def set_default_map(client: Robot, site_floor: SiteFloorModel) -> ResponseModel:
    """
    Set the default map for the robot.

    Args:
        client (Robot): API client
        site_floor (SiteFloorModel): Site and floor to set as default.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/mapping/default-map", data=site_floor.dict())
    return ResponseModel(**response)

def get_current_map(client: Robot) -> MapModel:
    """
    Get the robot's current map as a base64-encoded PNG.

    Args:
        client (Robot): API client

    Returns:
        MapModel: Current map information
    """
    response = client.get("/api/v1/mapping/map")
    return MapModel(**response)

def get_selected_map(client: Robot, site: str, floor: str) -> MapModel:
    """
    Get the selected map for a specific site and floor as a base64-encoded PNG.

    Args:
        client (Robot): API client
        site (str): The map's site.
        floor (str): The map's floor.

    Returns:
        MapModel: Selected map information
    """
    response = client.get(f"/api/v1/mapping/{site}/{floor}")
    return MapModel(**response)

def delete_selected_map(client: Robot, site: str, floor: str) -> ResponseModel:
    """
    Delete the selected map for a specific site and floor.

    Args:
        client (Robot): API client
        site (str): The map's site.
        floor (str): The map's floor.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.delete(f"/api/v1/mapping/{site}/{floor}")
    return ResponseModel(**response)

def start_mapping(client: Robot, mapping_model: MappingModel) -> ResponseModel:
    """
    Start the mapping process for the robot.

    Args:
        client (Robot): API client
        mapping_model (MappingModel): Mapping information.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/mapping/start", data=mapping_model.dict())
    return ResponseModel(**response)

def cancel_mapping(client: Robot) -> ResponseModel:
    """
    Cancel the robot's current mapping process.

    Args:
        client (Robot): API client

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/mapping/cancel")
    return ResponseModel(**response)

def change_map(client: Robot, site_floor: SiteFloorModel) -> ResponseModel:
    """
    Change the robot's current map to a new site and floor.

    Args:
        client (Robot): API client
        site_floor (SiteFloorModel): New site and floor for the map.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/mapping/change", data=site_floor.dict())
    return ResponseModel(**response)

def start_remapping(client: Robot, site_floor: SiteFloorModel) -> ResponseModel:
    """
    Start the remapping process for the robot.

    Args:
        client (Robot): API client
        site_floor (SiteFloorModel): Site and floor information for remapping.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/mapping/remap", data=site_floor.dict())
    return ResponseModel(**response)

def save_map(client: Robot) -> ResponseModel:
    """
    Save the robot's current map.

    Args:
        client (Robot): API client

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/mapping/save")
    return ResponseModel(**response)