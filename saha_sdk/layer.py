from .client import Robot
from .models import LayersModel, ResponseModel
from typing import List

def get_all_layers(client: Robot) -> List[LayersModel]:
    """
    Get the list of all layers of the robot.

    Args:
        client (Robot): API client

    Returns:
        List[LayersModel]: List of all layers
    """
    response = client.get("/api/v1/layers")
    return [LayersModel(**item) for item in response]

def get_layers_by_site(client: Robot, site: str) -> List[LayersModel]:
    """
    Get the list of layers filtered by site.

    Args:
        client (Robot): API client
        site (str): Site to filter layers by.

    Returns:
        List[LayersModel]: List of layers for the specified site
    """
    response = client.get(f"/api/v1/layers/{site}")
    return [LayersModel(**item) for item in response]

def get_layers_by_site_and_floor(client: Robot, site: str, floor: str) -> List[LayersModel]:
    """
    Get the list of layers filtered by site and floor.

    Args:
        client (Robot): API client
        site (str): Site to filter layers by.
        floor (str): Floor to filter layers by.

    Returns:
        List[LayersModel]: List of layers for the specified site and floor
    """
    response = client.get(f"/api/v1/layers/{site}/{floor}")
    return [LayersModel(**item) for item in response]

def get_layer(client: Robot, site: str, floor: str, uid: str) -> LayersModel:
    """
    Get a specific layer by its site, floor, and UID.

    Args:
        client (Robot): API client
        site (str): The layer's site.
        floor (str): The layer's floor.
        uid (str): The layer's UID.

    Returns:
        LayersModel: Requested layer information
    """
    response = client.get(f"/api/v1/layers/{site}/{floor}/{uid}")
    return LayersModel(**response)