"""
Go to Target and Speak Example

This example sends the robot to a specific target and, upon arrival,
makes it say "Hello World".
"""

import time
from saha_sdk.client import Robot
from saha_sdk import task, ui, status
from saha_sdk.models import SpeechModel, TaskRequestModel

# Robot connection
robot = Robot("http://192.168.1.100:5000")

# Target information
TARGET_NAME = "target_01"  # UID of your target
TARGET_UID = f"site_floor_{TARGET_NAME}"

print("=" * 50)
print("Robot Goes to Target and Speaks")
print("=" * 50)

try:
    # 1. Send go-to-target command
    print(f"\n[1/3] Going to target: {TARGET_NAME}")
    req = TaskRequestModel(
        type="TABLE_SERVICE",
        target_uid=TARGET_UID,
        activate=True,
        payload=[
            True,
            False,
            False,
            False
        ]
    )
    response = task.create_task(robot, req)

    if response.success:
        print(f"✓ {response.message}")
    else:
        print(f"✗ Hata: {response.message}")
        exit(1)

    # 2. Wait until the robot reaches the target
    print("\n[2/3] Waiting to reach the target...")
    print("(You can cancel with Ctrl+C)")

    current_state = ""
    while not current_state == "AtTheService":
        time.sleep(2)  # wait 2 seconds

        # Check robot status
        robot_status = status.get_robot_status(robot)
        current_state = robot_status.current_state
        print(f"  - Current state: {current_state}")

    # 3. Say "Hello World"
    print("\n[3/3] Robot is speaking...")
    speech = SpeechModel(
        lang="en",  # English
        text="Hello World! I am Saha Robot, I have reached the target successfully."
    )

    speech_response = ui.speak_text(robot, speech)

    if speech_response.success:
        print("✓ Robot spoke: 'Hello World!'")
    else:
        print(f"✗ Speech error: {speech_response.message}")

    print("\n" + "=" * 50)
    print("Task completed! 🎉")
    print("=" * 50)

except KeyboardInterrupt:
    print("\n\n⚠ Cancelled by user.")
    # Stop the robot
    print("Stopping robot...")
    from saha_sdk.models import RobotStopModel
    stop_model = RobotStopModel(stop=True)
    navigation.set_emergency_stop(robot, stop_model)
    print("✓ Robot stopped.")

except Exception as e:
    print(f"\n✗ An error occurred: {e}")
    import traceback
    traceback.print_exc()
