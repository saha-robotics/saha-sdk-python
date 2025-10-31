"""
Start Cruise Example

This example demonstrates starting a cruise (patrol route) on the robot.
"""

from saha_sdk.client import Robot
from saha_sdk import cruise
from saha_sdk.models import CruiseControlRequestModel

# Robot connection
robot = Robot("http://192.168.1.100:5000")

print("=" * 60)
print("Start Cruise")
print("=" * 60)

try:
    # 1. List existing cruises
    print("\n[1/3] Listing existing cruises...")
    all_cruises = cruise.get_all_cruises(robot)

    if not all_cruises:
        print("⚠ No cruises found. You should create a cruise first.")
        exit(1)

    print(f"✓ Found {len(all_cruises)} cruises:\n")
    for i, c in enumerate(all_cruises, 1):
        print(f"{i}. {c.name}")
        print(f"   Site: {c.site_floor.site}, Floor: {c.site_floor.floor}")
        print(f"   Number of waypoints: {len(c.waypoints)}")
        print()

    # 2. Get default cruise route
    print("[2/3] Checking default cruise route...")
    try:
        default_route = cruise.get_default_cruise_route(robot)
        print(f"✓ Default route: {default_route.route}")
    except Exception as e:
        print(f"⚠ Default route not found: {e}")
        default_route = None

    # 3. Start cruise
    print("\n[3/3] Starting cruise...")

    # Use the first cruise or the default route
    cruise_name = all_cruises[0].name if all_cruises else ""

    cruise_control = CruiseControlRequestModel(
        cruise_cmd="CMD_START",
        cruise_route=cruise_name if cruise_name else "",  # If empty, default route is used
        number_of_rounds=2  # Do 2 rounds
    )

    response = cruise.start_cruise(robot, cruise_control)

    if response.success:
        print(f"✓ {response.message}")
        print(f"\nCruise started: {cruise_name if cruise_name else 'default route'}")
        print("Robot started patrolling! 🚀")
    else:
        print(f"✗ Error: {response.message}")

    print("\n" + "=" * 60)
    print("You can stop the cruise using the CMD_STOP command.")
    print("=" * 60)

except Exception as e:
    print(f"\n✗ Error: {e}")
    import traceback
    traceback.print_exc()
