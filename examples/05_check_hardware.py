"""
Hardware Status Check Example

This example checks the status of the robot's hardware components.
"""

from saha_sdk.client import Robot
from saha_sdk import status

# Robot connection
robot = Robot("http://192.168.1.100:5000")

print("=" * 60)
print("Robot Hardware Status")
print("=" * 60)

try:
    # Get hardware status
    hw_status = status.get_hardware_status(robot)

    # LIDAR sensors
    print("\n📡 LIDAR Sensors:")
    if hw_status.lidars:
        for lidar in hw_status.lidars:
            status_icon = "✓" if lidar.is_working else "✗"
            print(f"  {status_icon} {lidar.name}")
            print(f"     Status: {lidar.state}")
            if lidar.error:
                print(f"     Error: {lidar.error}")
    else:
        print("  ⚠ No LIDAR information")

    # Camera sensors
    print("\n📷 Cameras:")
    if hw_status.cameras:
        for camera in hw_status.cameras:
            status_icon = "✓" if camera.is_working else "✗"
            print(f"  {status_icon} {camera.name}")
            print(f"     Status: {camera.state}")
            if camera.error:
                print(f"     Error: {camera.error}")
    else:
        print("  ⚠ No camera information")

    # Internet connection
    print("\n🌐 Internet Connection:")
    internet = hw_status.internet_status
    print(f"  Status: {internet.state}")

    if internet.wifi_enabled:
        wifi_icon = "✓" if internet.wifi_connected else "✗"
        print(f"  {wifi_icon} Wi-Fi")
        if internet.wifi_connected:
            print(f"     SSID: {internet.wifi_ssid}")
            print(f"     IP: {internet.wifi_ip_addr}")
            print(f"     MAC: {internet.wifi_mac_addr}")
    else:
        print("  ⚠ Wi-Fi disabled")

    if internet.mobile_enabled:
        mobile_icon = "✓" if internet.mobile_connected else "✗"
        print(f"  {mobile_icon} Mobile data")

    print("\n" + "=" * 60)
    print("All hardware components have been checked! ✓")
    print("=" * 60)

except Exception as e:
    print(f"\n✗ Error: {e}")
    import traceback
    traceback.print_exc()
