# saharobotik/layer.py

from .client import SahaRobotikClient


def get_all_layers(client: SahaRobotikClient):
    """
    Lists all layer data in the system.

    Args:
        client (SahaRobotikClient): API client

    Returns:
        dict: List of layers
    """
    return client.get("/api/v1/layers")


def get_layers_by_site(client: SahaRobotikClient, site: str):
    """
    Retrieves all layers defined for a specific site.

    Args:
        client (SahaRobotikClient): API client
        site (str): Site name

    Returns:
        dict: Layers belonging to the specified site
    """
    return client.get(f"/api/v1/layers/{site}")


def get_layers_by_floor(client: SahaRobotikClient, site: str, floor: str):
    """
    Retrieves layers defined for a specific site and floor.

    Args:
        client (SahaRobotikClient): API client
        site (str): Site name
        floor (str): Floor name

    Returns:
        dict: List of layers based on the specified floor
    """
    return client.get(f"/api/v1/layers/{site}/{floor}")


def get_layer_by_uid(client: SahaRobotikClient, site: str, floor: str, uid: str):
    """
    Retrieves detailed layer data for a specific layer UID.

    Args:
        client (SahaRobotikClient): API client
        site (str): Site name
        floor (str): Floor name
        uid (str): Unique identifier (UID) of the layer

    Returns:
        dict: Detailed layer data
    """
    return client.get(f"/api/v1/layers/{site}/{floor}/{uid}")
