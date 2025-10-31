from .client import Robot
from .models import RobotRouteModel, CruiseModel, CruiseRequestModel, CruiseControlRequestModel, ResponseModel
from typing import List

def get_default_cruise_route(client: Robot) -> RobotRouteModel:
    """
    Get the default cruise route for the robot.

    Args:
        client (Robot): API client

    Returns:
        RobotRouteModel: Default cruise route information
    """
    response = client.get("/api/v1/config/default-route")
    return RobotRouteModel(**response)

def set_default_cruise_route(client: Robot, route_model: RobotRouteModel) -> ResponseModel:
    """
    Set the default cruise route for the robot.

    Args:
        client (Robot): API client
        route_model (RobotRouteModel): Route to set as default.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/config/default-route", data=route_model.dict())
    return ResponseModel(**response)

def get_all_cruises(client: Robot) -> List[CruiseModel]:
    """
    Get the list of all cruises for the robot.

    Args:
        client (Robot): API client

    Returns:
        List[CruiseModel]: List of all cruises
    """
    response = client.get("/api/v1/cruises")
    return [CruiseModel(**item) for item in response]

def add_cruise(client: Robot, cruise_request: CruiseRequestModel) -> ResponseModel:
    """
    Add a new cruise to the robot.

    Args:
        client (Robot): API client
        cruise_request (CruiseRequestModel): Cruise information to add.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/cruises", data=cruise_request.dict())
    return ResponseModel(**response)

def start_cruise(client: Robot, cruise_control_request: CruiseControlRequestModel) -> ResponseModel:
    """
    Start a cruise on the robot.

    Args:
        client (Robot): API client
        cruise_control_request (CruiseControlRequestModel): Cruise control information.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/cruises/control", data=cruise_control_request.dict())
    return ResponseModel(**response)

def get_cruises_by_site(client: Robot, site: str) -> List[CruiseModel]:
    """
    Get the list of cruises filtered by site.

    Args:
        client (Robot): API client
        site (str): Site to filter cruises by.

    Returns:
        List[CruiseModel]: List of cruises for the specified site
    """
    response = client.get(f"/api/v1/cruises/{site}")
    return [CruiseModel(**item) for item in response]

def get_cruises_by_site_and_floor(client: Robot, site: str, floor: str) -> List[CruiseModel]:
    """
    Get the list of cruises filtered by site and floor.

    Args:
        client (Robot): API client
        site (str): Site to filter cruises by.
        floor (str): Floor to filter cruises by.

    Returns:
        List[CruiseModel]: List of cruises for the specified site and floor
    """
    response = client.get(f"/api/v1/cruises/{site}/{floor}")
    return [CruiseModel(**item) for item in response]

def get_cruise(client: Robot, site: str, floor: str, name: str) -> CruiseModel:
    """
    Get a specific cruise by its site, floor, and name.

    Args:
        client (Robot): API client
        site (str): The cruise's site.
        floor (str): The cruise's floor.
        name (str): The cruise's name.

    Returns:
        CruiseModel: Requested cruise information
    """
    response = client.get(f"/api/v1/cruises/{site}/{floor}/{name}")
    return CruiseModel(**response)

def update_cruise(client: Robot, site: str, floor: str, name: str, cruise_request: CruiseRequestModel) -> ResponseModel:
    """
    Update a specific cruise by name.

    Args:
        client (Robot): API client
        site (str): The cruise's site.
        floor (str): The cruise's floor.
        name (str): The cruise's name.
        cruise_request (CruiseRequestModel): Updated cruise information.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.patch(f"/api/v1/cruises/{site}/{floor}/{name}", data=cruise_request.dict())
    return ResponseModel(**response)

def delete_cruise(client: Robot, site: str, floor: str, name: str) -> ResponseModel:
    """
    Delete a specific cruise by name.

    Args:
        client (Robot): API client
        site (str): The cruise's site.
        floor (str): The cruise's floor.
        name (str): The cruise's name.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.delete(f"/api/v1/cruises/{site}/{floor}/{name}")
    return ResponseModel(**response)