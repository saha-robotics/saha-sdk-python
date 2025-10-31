from .client import Robot
from .models import TaskModel, TaskRequestModel, ResponseModel
from typing import List

def get_all_tasks(client: Robot) -> List[TaskModel]:
    """
    Retrieve the list of all tasks of the robot.

    Args:
        client (Robot): API client

    Returns:
        List[TaskModel]: List of all tasks
    """
    response = client.get("/api/v1/tasks")
    return [TaskModel(**item) for item in response]

def create_task(client: Robot, task_request: TaskRequestModel) -> ResponseModel:
    """
    Create a new task or update an existing one.

    Args:
        client (Robot): API client
        task_request (TaskRequestModel): Task information to create or update.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/tasks", data=task_request.dict())
    return ResponseModel(**response)

def get_task(client: Robot, task_uid: str) -> TaskModel:
    """
    Retrieve a specific task by its ID.

    Args:
        client (Robot): API client
        task_uid (str): The UID of the task.

    Returns:
        TaskModel: The requested task information
    """
    response = client.get(f"/api/v1/tasks/{task_uid}")
    return TaskModel(**response)

def update_task(client: Robot, task_uid: str, task_request: TaskRequestModel) -> ResponseModel:
    """
    Update a specific task by its ID.

    Args:
        client (Robot): API client
        task_uid (str): The UID of the task.
        task_request (TaskRequestModel): Updated task information.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.patch(f"/api/v1/tasks/{task_uid}", data=task_request.dict())
    return ResponseModel(**response)

def delete_task(client: Robot, task_uid: str) -> ResponseModel:
    """
    Delete a specific task by its ID.

    Args:
        client (Robot): API client
        task_uid (str): The UID of the task.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.delete(f"/api/v1/tasks/{task_uid}")
    return ResponseModel(**response)

def pause_mission(client: Robot) -> ResponseModel:
    """
    Pause the robot's current mission.

    Args:
        client (Robot): API client

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/tasks/pause")
    return ResponseModel(**response)

def resume_mission(client: Robot) -> ResponseModel:
    """
    Resume the robot's paused mission.

    Args:
        client (Robot): API client

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/tasks/resume")
    return ResponseModel(**response)

def clear_all_tasks(client: Robot) -> ResponseModel:
    """
    Clear all tasks from the robot's mission.

    Args:
        client (Robot): API client

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/tasks/clear")
    return ResponseModel(**response)