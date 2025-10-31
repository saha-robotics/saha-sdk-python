from .client import Robot
from .models import TargetModel, TargetRequestModel, ResponseModel
from typing import List

def get_all_targets(client: Robot) -> List[TargetModel]:
    """
    Retrieve the list of all targets of the robot.

    Args:
        client (Robot): API client

    Returns:
        List[TargetModel]: List of all targets
    """
    response = client.get("/api/v1/targets")
    return [TargetModel(**item) for item in response]

def add_target(client: Robot, target_request: TargetRequestModel) -> ResponseModel:
    """
    Add a new target to the robot.

    Args:
        client (Robot): API client
        target_request (TargetRequestModel): Target information to add.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/targets", data=target_request.dict())
    return ResponseModel(**response)

def get_targets_by_site(client: Robot, site: str) -> List[TargetModel]:
    """
    Retrieve the list of targets filtered by site.

    Args:
        client (Robot): API client
        site (str): The site to filter targets by.

    Returns:
        List[TargetModel]: List of targets for the specified site
    """
    response = client.get(f"/api/v1/targets/{site}")
    return [TargetModel(**item) for item in response]

def get_targets_by_site_and_floor(client: Robot, site: str, floor: str) -> List[TargetModel]:
    """
    Retrieve the list of targets filtered by site and floor.

    Args:
        client (Robot): API client
        site (str): The site to filter targets by.
        floor (str): The floor to filter targets by.

    Returns:
        List[TargetModel]: List of targets for the specified site and floor
    """
    response = client.get(f"/api/v1/targets/{site}/{floor}")
    return [TargetModel(**item) for item in response]

def get_target(client: Robot, site: str, floor: str, name: str) -> TargetModel:
    """
    Retrieve a specific target by its site, floor, and name.

    Args:
        client (Robot): API client
        site (str): The site of the target.
        floor (str): The floor of the target.
        name (str): The name of the target.

    Returns:
        TargetModel: The requested target information
    """
    response = client.get(f"/api/v1/targets/{site}/{floor}/{name}")
    return TargetModel(**response)

def update_target(client: Robot, site: str, floor: str, name: str, target_request: TargetRequestModel) -> ResponseModel:
    """
    Update a specific target by its site, floor, and name.

    Args:
        client (Robot): API client
        site (str): The site of the target.
        floor (str): The floor of the target.
        name (str): The name of the target.
        target_request (TargetRequestModel): Updated target information.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.patch(f"/api/v1/targets/{site}/{floor}/{name}", data=target_request.dict())
    return ResponseModel(**response)

def delete_target(client: Robot, site: str, floor: str, name: str) -> ResponseModel:
    """
    Delete a specific target by its site, floor, and name.

    Args:
        client (Robot): API client
        site (str): The site of the target.
        floor (str): The floor of the target.
        name (str): The name of the target.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.delete(f"/api/v1/targets/{site}/{floor}/{name}")
    return ResponseModel(**response)