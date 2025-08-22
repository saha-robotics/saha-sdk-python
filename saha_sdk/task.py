# saharobotik/task.py

from .client import SahaRobotikClient


def get_all_tasks(client: SahaRobotikClient):
    """
    Retrieves all tasks defined in the system.

    Args:
        client (Robot): API client

    Returns:
        dict: List of tasks
    """
    return client.get("/api/v1/tasks")


def create_or_update_task(client: SahaRobotikClient, task_data: dict):
    """
    Creates or updates a task with full task specification.

    Args:
        client (Robot): API client
        task_data (dict): Task body. Should include:
            - timeout (int)
            - type (str): e.g., "TABLE_SERVICE"
            - activate (bool)
            - task_index (int)
            - target_uid (str)
            - payload (list[bool])
            - celebrating_name (str)

    Returns:
        dict: API response
    """
    return client.post("/api/v1/tasks", data=task_data)



def get_task_by_id(client: SahaRobotikClient, task_uid: str):
    """
    Retrieves a specific task by its UID.

    Args:
        client (Robot): API client
        task_uid (str): Unique identifier of the task

    Returns:
        dict: Task information
    """
    return client.get(f"/api/v1/tasks/{task_uid}")


def update_task(client: SahaRobotikClient, task_uid: str, update_data: dict):
    """
    Updates a specific task by UID.

    Args:
        client (Robot): API client
        task_uid (str): Unique identifier of the task to update
        update_data (dict): Fields to be updated. Should include:
            - timeout (int)
            - type (str): e.g., "TABLE_SERVICE"
            - activate (bool)
            - task_index (int)
            - target_uid (str)
            - payload (list[bool])
            - celebrating_name (str)

    Returns:
        dict: API response
    """
    return client.patch(f"/api/v1/tasks/{task_uid}", data=update_data)


def delete_task(client: SahaRobotikClient, task_uid: str):
    """
    Deletes a specific task.

    Args:
        client (Robot): API client
        task_uid (str): Identifier of the task to delete

    Returns:
        dict: Result of the deletion
    """
    return client.delete(f"/api/v1/tasks/{task_uid}")


def pause_task(client: SahaRobotikClient):
    """
    Temporarily pauses the robot's current task.

    Args:
        client (Robot): API client

    Returns:
        dict: Result of the pause operation
    """
    return client.post("/api/v1/task/pause")
