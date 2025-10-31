"""
Basic Connection Example

This example shows how to connect to the Saha Robotik API.
"""

from saha_sdk.client import Robot
from saha_sdk import status

# Create the robot client (with base_url only)
robot = Robot("http://192.168.1.100:5000")

# If an API key is required, you can add it later:
# robot.set_api_key("your-api-key-here")

# Check robot status
try:
    robot_status = status.get_robot_status(robot)
    print("✓ Robot connection successful!")
    print(f"  Battery: {robot_status.battery_percent}%")
    print(f"  Charging: {'Charging' if robot_status.is_charging else 'Not charging'}")
    print(f"  Current state: {robot_status.current_state}")

    # Retrieve robot information
    robot_info = status.get_robot_info(robot)
    print(f"  Robot ID: {robot_info.robot_uid}")
    print(f"  Site: {robot_info.site_floor.site}")
    print(f"  Floor: {robot_info.site_floor.floor}")

except Exception as e:
    print(f"✗ Connection error: {e}")
