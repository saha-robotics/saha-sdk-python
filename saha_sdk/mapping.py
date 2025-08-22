# saharobotik/mapping.py

from .client import SahaRobotikClient

def get_all_maps(client: SahaRobotikClient):
    """
    Retrieves all maps of the robot.

    Args:
        client (Robot): API client

    Returns:
        dict: List of maps
    """
    return client.get("/api/v1/mapping")

def get_default_map(client: SahaRobotikClient):
    """
    Retrieves the default map used by the robot.

    Args:
        client (Robot): API client

    Returns:
        dict: Default map data
    """
    return client.get("/api/v1/mapping/default-map")


def set_default_map(client: SahaRobotikClient, data: dict):
    """
    Sets the robot's default map.

    Args:
        client (Robot): API client
        data (dict): Map information (e.g., {"site": "Office", "floor": "0"})

    Returns:
        dict: Result of the operation
    """
    return client.post("/api/v1/mapping/default-map", data=data)


def get_current_map(client: SahaRobotikClient):
    """
    Retrieves the base64 encoded version of the map currently used by the robot.

    Args:
        client (Robot): API client

    Returns:
        dict: Base64 encoded PNG map data
    """
    return client.get("/api/v1/mapping/map")


def get_map_by_site_floor(client: SahaRobotikClient, site: str, floor: str):
    """
    Retrieves the map data registered for a specific site and floor.

    Args:
        client (Robot): API client
        site (str): Site name
        floor (str): Floor name

    Returns:
        dict: Map data (including base64 PNG)
    """
    return client.get(f"/api/v1/mapping/{site}/{floor}")


def delete_map(client: SahaRobotikClient, site: str, floor: str):
    """
    Deletes the map data for a specific site and floor.

    Args:
        client (Robot): API client
        site (str): Site name
        floor (str): Floor name

    Returns:
        dict: Result of the deletion operation
    """
    return client.delete(f"/api/v1/mapping/{site}/{floor}")


def start_mapping(client: SahaRobotikClient):
    """
    Starts a new mapping process.

    Args:
        client (Robot): API client

    Returns:
        dict: Result of the operation
    """
    return client.post("/api/v1/mapping/start")


def cancel_mapping(client: SahaRobotikClient):
    """
    Cancels the ongoing mapping process.

    Args:
        client (Robot): API client

    Returns:
        dict: Result of the cancellation
    """
    return client.post("/api/v1/mapping/cancel")


def change_map(client: SahaRobotikClient, data: dict):
    """
    Changes the map currently used by the robot.

    Args:
        client (Robot): API client
        data (dict): Map change information (e.g., {"site": "...", "floor": "..."})

    Returns:
        dict: Result of the map change operation
    """
    return client.post("/api/v1/mapping/change", data=data)


def remap(client: SahaRobotikClient):
    """
    Starts a remapping process on an existing map.

    Args:
        client (Robot): API client

    Returns:
        dict: Result of the remapping operation
    """
    return client.post("/api/v1/mapping/remap")


def save_map(client: SahaRobotikClient):
    """
    Saves the created map permanently.

    Args:
        client (Robot): API client

    Returns:
        dict: Result of the save operation
    """
    return client.post("/api/v1/mapping/save")
