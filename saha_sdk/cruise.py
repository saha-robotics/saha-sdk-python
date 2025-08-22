# saharobotik/cruise.py

from .client import Robot


def get_all_cruises(client: Robot):
    """
    Retrieves all routes defined for the robot.

    Args:
        client (Robot): API client

    Returns:
        dict: All routes
    """
    return client.get("/api/v1/cruises")


def add_cruise(client: Robot, name: str, waypoints: list[str], site: str, floor: str):
    """
    Adds a new cruise route.

    Args:
        client (Robot): API client
        name (str): Name of the cruise route
        waypoints (list[str]): List of waypoint identifiers on the route
        site (str): Site name
        floor (str): Floor name

    Returns:
        dict: Result of the operation
    """
    cruise_data = {
        "name": name,
        "waypoints": waypoints,
        "site": site,
        "floor": floor
    }
    return client.post("/api/v1/cruises", data=cruise_data)

def get_cruises_by_site(client: Robot, site: str):
    """
    Retrieves routes defined for a specific site.

    Args:
        client (Robot): API client
        site (str): Site name

    Returns:
        dict: Routes belonging to the specified site
    """
    return client.get(f"/api/v1/cruises/{site}")


def get_cruises_by_floor(client: Robot, site: str, floor: str):
    """
    Retrieves routes defined for a specific site and floor.

    Args:
        client (Robot): API client
        site (str): Site name
        floor (str): Floor name

    Returns:
        dict: Routes based on the specified floor
    """
    return client.get(f"/api/v1/cruises/{site}/{floor}")


def get_cruise_by_name(client: Robot, site: str, floor: str, name: str):
    """
    Retrieves a specific route by site, floor, and name.

    Args:
        client (Robot): API client
        site (str): Site name
        floor (str): Floor name
        name (str): Route name

    Returns:
        dict: The requested route
    """
    return client.get(f"/api/v1/cruises/{site}/{floor}/{name}")


def update_cruise(client: Robot, site: str, floor: str, name: str, cruise_data: dict):
    """
    Updates a specific route.

    Args:
        client (Robot): API client
        site (str): Site name
        floor (str): Floor name
        name (str): Route name
        cruise_data (dict): Updated route information

    Returns:
        dict: Update result
    """
    return client.patch(f"/api/v1/cruises/{site}/{floor}/{name}", data=cruise_data)


def delete_cruise(client: Robot, site: str, floor: str, name: str):
    """
    Deletes a specific route.

    Args:
        client (Robot): API client
        site (str): Site name
        floor (str): Floor name
        name (str): Route name

    Returns:
        dict: Deletion result
    """
    return client.delete(f"/api/v1/cruises/{site}/{floor}/{name}")


def get_default_cruise_route(client: Robot):
    """
    Retrieves the robot's default route.

    Args:
        client (Robot): API client

    Returns:
        dict: Default route information
    """
    return client.get("/api/v1/config/default-route")


def set_default_cruise_route(client: Robot, route_data: dict):
    """
    Sets the robot's default route.

    Args:
        client (Robot): API client
        route_data (dict): Route information to be set as default
            {
              "route": "Route Name"
            }

    Returns:
        dict: Result of the operation
    """
    return client.post("/api/v1/config/default-route", data=route_data)
