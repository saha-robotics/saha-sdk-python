# saharobotik/targets.py

from .client import SahaRobotikClient


def get_all_targets(client: SahaRobotikClient):
    """
    Retrieves all defined target points of the robot.

    Args:
        client (Robot): API client

    Returns:
        dict: List of all targets
    """
    return client.get("/api/v1/targets")


def add_target(client: SahaRobotikClient, target_data: dict):
    """
    Defines a new target.

    Args:
        client (Robot): API client
        target_data (dict): Target information (e.g., site, floor, name, pose, etc.)

    Returns:
        dict: Result of the creation
    """
    return client.post("/api/v1/targets", data=target_data)


def get_targets_by_site(client: SahaRobotikClient, site: str):
    """
    Retrieves targets within a specific site.

    Args:
        client (Robot): API client
        site (str): Site name

    Returns:
        dict: Targets belonging to the site
    """
    return client.get(f"/api/v1/targets/{site}")


def get_targets_by_floor(client: SahaRobotikClient, site: str, floor: str):
    """
    Retrieves targets defined for a specific site and floor.

    Args:
        client (Robot): API client
        site (str): Site name
        floor (str): Floor name

    Returns:
        dict: List of targets by floor
    """
    return client.get(f"/api/v1/targets/{site}/{floor}")


def get_target_by_name(client: SahaRobotikClient, site: str, floor: str, name: str):
    """
    Retrieves a specific target by site, floor, and name.

    Args:
        client (Robot): API client
        site (str): Site name
        floor (str): Floor name
        name (str): Target name

    Returns:
        dict: Target information
    """
    return client.get(f"/api/v1/targets/{site}/{floor}/{name}")


def update_target(client: SahaRobotikClient, site: str, floor: str, name: str, update_data: dict):
    """
    Updates information of an existing target.

    Args:
        client (Robot): API client
        site (str): Site name
        floor (str): Floor name
        name (str): Target name
        update_data (dict): Updated fields

    Returns:
        dict: Result of the update
    """
    return client.patch(f"/api/v1/targets/{site}/{floor}/{name}", data=update_data)


def delete_target(client: SahaRobotikClient, site: str, floor: str, name: str):
    """
    Deletes a specific target from the system.

    Args:
        client (Robot): API client
        site (str): Site name
        floor (str): Floor name
        name (str): Target name

    Returns:
        dict: Result of the deletion
    """
    return client.delete(f"/api/v1/targets/{site}/{floor}/{name}")
