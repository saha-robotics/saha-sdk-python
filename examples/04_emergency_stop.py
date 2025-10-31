"""
Emergency Stop Example

This example shows how to immediately stop the robot.
"""

from saha_sdk.client import Robot
from saha_sdk import navigation
from saha_sdk.models import RobotStopModel

# Robot connection
robot = Robot("http://192.168.1.100:5000")

print("=" * 60)
print("Emergency Stop")
print("=" * 60)

try:
    # Check current emergency stop status
    print("\n[1/3] Checking current emergency stop status...")
    stop_status = navigation.get_emergency_stop_status(robot)

    if stop_status.stop:
        print("⚠ The robot is already stopped!")
    else:
        print("✓ The robot is currently running.")

    # Activate emergency stop
    print("\n[2/3] Activating emergency stop...")
    stop_model = RobotStopModel(stop=True)
    response = navigation.set_emergency_stop(robot, stop_model)

    if response.success:
        print("✓ Robot performed an emergency stop! 🛑")
    else:
        print(f"✗ Error: {response.message}")

    # Check status again
    print("\n[3/3] Re-checking status...")
    stop_status = navigation.get_emergency_stop_status(robot)

    if stop_status.stop:
        print("✓ Emergency stop is active.")
        print("\n💡 To resume the robot:")
        print("   stop_model = RobotStopModel(stop=False)")
        print("   navigation.set_emergency_stop(robot, stop_model)")
    else:
        print("⚠ Emergency stop is not active.")

    print("\n" + "=" * 60)

except Exception as e:
    print(f"\n✗ Error: {e}")
    import traceback
    traceback.print_exc()
