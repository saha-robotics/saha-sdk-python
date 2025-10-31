"""
List Targets Example

This example lists all robot targets and shows their details.
"""

from saha_sdk.client import Robot
from saha_sdk import targets

# Robot connection
robot = Robot("http://192.168.1.100:5000")

print("=" * 60)
print("Robot Hedefleri Listesi")
print("=" * 60)

try:
    # Fetch all targets
    all_targets = targets.get_all_targets(robot)

    if not all_targets:
        print("\n⚠ No targets have been saved yet.")
    else:
        print(f"\nA total of {len(all_targets)} targets were found:\n")

        for i, target in enumerate(all_targets, 1):
            print(f"{i}. {target.name}")
            print(f"   UID: {target.uid}")
            print(f"   Site: {target.site_floor.site}, Floor: {target.site_floor.floor}")
            print(f"   Position: x={target.px:.2f}m, y={target.py:.2f}m")
            print(f"   Orientation: {target.yaw_deg:.1f}°")
            print(f"   Type: {target.type}")
            print(f"   Tolerance: {target.tol}m")
            print()

    # Site-based filtering example
    print("-" * 60)
    print("Site-Based Filtering")
    print("-" * 60)

    # Example site name (change as needed)
    example_site = "site1"

    try:
        site_targets = targets.get_targets_by_site(robot, example_site)
        print(f"\nThere are {len(site_targets)} targets in site '{example_site}':")
        for target in site_targets:
            print(f"  • {target.name} ({target.type})")
    except Exception as e:
        print(f"\n⚠ No targets found for '{example_site}': {e}")

except Exception as e:
    print(f"\n✗ Error: {e}")
    import traceback
    traceback.print_exc()
