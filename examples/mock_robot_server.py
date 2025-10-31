"""
Mock Robot API Server

Simple mock server to test the SDK without a real robot.

Usage:
    python mock_robot_server.py

Then in another terminal:
    python 02_go_to_target_and_speak.py
"""

from flask import Flask, jsonify, request
import time

app = Flask(__name__)

# Mock state
robot_state = {
    "current_state": "READY",
    "battery_percent": 85.0,
    "is_charging": False,
    "is_estopped": False,
    "position": {"x": 0.0, "y": 0.0, "theta": 0.0},
    "target_state": None,  # None, "MOVING", "REACHED"
    "target_start_time": None
}


# Status endpoints
@app.route('/api/v1/status', methods=['GET'])
def get_status():
    return jsonify({
        "is_charging": robot_state["is_charging"],
        "battery_percent": robot_state["battery_percent"],
        "is_estopped": robot_state["is_estopped"],
        "current_state": robot_state["current_state"],
        "out_of_service": False
    })


@app.route('/api/v1/status/info', methods=['GET'])
def get_info():
    return jsonify({
        "robot_uid": "mock_robot_001",
        "project_id": "test_project",
        "site_floor": {"site": "BVKoridor", "floor": "0"}
    })


@app.route('/api/v1/status/hardware', methods=['GET'])
def get_hardware():
    return jsonify({
        "lidars": [{
            "name": "main_lidar",
            "is_working": True,
            "state": "WORKING",
            "error": ""
        }],
        "cameras": [{
            "name": "front_camera",
            "is_working": True,
            "state": "WORKING",
            "error": ""
        }],
        "internet_status": {
            "state": "CONNECTED",
            "error": "",
            "wifi_enabled": True,
            "wifi_connected": True,
            "wifi_ssid": "MockNetwork",
            "wifi_ip_addr": "192.168.1.100",
            "wifi_mac_addr": "00:11:22:33:44:55",
            "mobile_enabled": False,
            "mobile_connected": False
        }
    })


# Navigation endpoints
@app.route('/api/v1/navigation/position', methods=['GET'])
def get_position():
    # Simulate: move towards the target
    if robot_state["target_state"] == "MOVING":
        elapsed = time.time() - robot_state["target_start_time"]
        # Reach the target in 10 seconds
        progress = min(elapsed / 10.0, 1.0)
        robot_state["position"]["x"] = progress * 5.0
        robot_state["position"]["y"] = progress * 3.0

        if progress >= 1.0:
            robot_state["target_state"] = "REACHED"
            robot_state["current_state"] = "READY"

    return jsonify({
        "position": robot_state["position"],
        "twist": {"vel_x": 0.0, "vel_z": 0.0}
    })


@app.route('/api/v1/navigation/goal/target', methods=['POST'])
def set_goal_target():
    data = request.json
    target_uid = data.get("target_uid", "")

    print(f"\n✓ Target received: {target_uid}")
    print(f"  Robot will move towards the target...")

    # Begin simulated movement to target
    robot_state["target_state"] = "MOVING"
    robot_state["current_state"] = "MOVING_TO_TARGET"
    robot_state["target_start_time"] = time.time()

    return jsonify({
        "success": True,
        "message": f"Moving to target: {target_uid}"
    })


@app.route('/api/v1/navigation/stop', methods=['GET'])
def get_stop_status():
    return jsonify({
        "stop": robot_state["is_estopped"]
    })


@app.route('/api/v1/navigation/stop', methods=['POST'])
def set_stop():
    data = request.json
    stop = data.get("stop", False)
    robot_state["is_estopped"] = stop
    robot_state["current_state"] = "STOPPED" if stop else "READY"

    print(f"\n{'✓ Robot stopped!' if stop else '✓ Robot continues!'}")

    return jsonify({
        "success": True,
        "message": "Emergency stop set" if stop else "Emergency stop released"
    })


# UI endpoints
@app.route('/api/v1/ui/speech', methods=['POST'])
def speak():
    data = request.json
    text = data.get("text", "")
    lang = data.get("lang", "en")

    print(f"\n🔊 Robot speaking ({lang}): '{text}'")

    return jsonify({
        "success": True,
        "message": "Speech sent"
    })


# Targets endpoints
@app.route('/api/v1/targets', methods=['GET'])
def get_targets():
    return jsonify([
        {
            "name": "Table1",
            "uid": "BVCorridor_0_Table1",
            "site_floor": {"site": "BVCorridor", "floor": "0"},
            "eg": "",
            "eg_dir": "",
            "px": 5.0,
            "py": 3.0,
            "yaw_deg": 90.0,
            "tol": 0.5,
            "type": "default",
            "label": "{}",
            "cid": ""
        },
        {
            "name": "Table2",
            "uid": "BVCorridor_0_Table2",
            "site_floor": {"site": "BVCorridor", "floor": "0"},
            "eg": "",
            "eg_dir": "",
            "px": 10.0,
            "py": 5.0,
            "yaw_deg": 180.0,
            "tol": 0.5,
            "type": "default",
            "label": "{}",
            "cid": ""
        }
    ])


# Health check
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "message": "Mock Robot API Server is running"})


if __name__ == '__main__':
    print("=" * 60)
    print("Mock Robot API Server")
    print("=" * 60)
    print("\nStarting server...")
    print("URL: http://localhost:7242")
    print("\nTo test examples:")
    print("  1. Keep this server running")
    print("  2. Run the examples in another terminal")
    print("\nStop with Ctrl+C\n")
    print("=" * 60 + "\n")

    app.run(host='0.0.0.0', port=7242, debug=True)
