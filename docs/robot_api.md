# Getting Started

## Service Robot API Documentation

This documentation describes how to interact with the **Saha Robotik Python Library**, a wrapper around the RESTful API developed to control, manage, and monitor a service robot. The library enables easy access to various robot functions — from status monitoring to complex task scheduling — through intuitive Python functions.

This document reflects the updated API structure and usage patterns as implemented in the Python library.

---

## 🤖 Robot Status

### `get_robot_status(client)`

**GET /api/v1/status**
Returns the robot's general operational status including:

* `battery_percent`
* `is_charging`
* `is_estopped`
* `state` (e.g., `READY_FOR_MISSION`)

### `get_hardware_status(client)`

**GET /api/v1/status/hardware**
Reports hardware component health (Lidar, camera, internet).

---

## 🧭 Navigation

### `get_navigation_path(client)` / `get_navigation_path_stream(client)`

**GET /api/v1/navigation/path**
**GET /api/v1/navigation/path/stream**
Fetch the robot's current planned path.

### `get_current_position(client)` / `get_position_stream(client)`

**GET /api/v1/navigation/position**
**GET /api/v1/navigation/position/stream**
Get the robot's real-time location (x, y, theta).

### `set_goal_pose(client, x, y, theta)`

**POST /api/v1/navigation/goal/pose**
Send coordinate goal.

### `set_goal_target(client, target_uid)`

**POST /api/v1/navigation/goal/target**
Send robot to predefined target.

### `send_velocity_command(client, vel_data)`

**POST /api/v1/navigation/vel**
Send direct movement commands.

### `send_safe_velocity(client, vel_data)`

**POST /api/v1/navigation/vel/safe**
Send limited, safety-checked movement.

### `stop_robot(client)`

**POST /api/v1/navigation/stop**
Emergency stop.

### `start_localization(client)`

**POST /api/v1/navigation/localization**
Re-localize the robot on the map.

---

## ⚙️ Profile and Mode

### `get_profiles(client)`

**GET /api/v1/profile**
Fetch current behavior/environment/speed profiles.

### `set_environment_profile(client, profile_name)`

**POST /api/v1/profile/environment**

### `set_behavior_profile(client, profile_name)`

**POST /api/v1/profile/behavior**

### `set_speed_profile(client, profile_name)`

**POST /api/v1/profile/speed**
Adjust robot behavior dynamically.

### `get_modes(client)`

**GET /api/v1/mode**
Fetch list of available robot modes.

### `set_mode(client, mode_data)`

**POST /api/v1/mode**
Set a special operational mode.

### `delete_mode(client, name)`

**DELETE /api/v1/mode/{name}**
Remove a robot mode.

---

## 🗺️ Mapping

### `get_maps(client)`

**GET /api/v1/mapping**
List available maps.

### `get_default_map(client)` / `set_default_map(client, map_data)`

**GET /api/v1/mapping/default-map**
**POST /api/v1/mapping/default-map**
Manage default map.

### `get_current_map(client)`

**GET /api/v1/mapping/map**
Returns base64-encoded map PNG.

### `get_map_by_site_floor(client, site, floor)`

**GET /api/v1/mapping/{site}/{floor}**
Fetch specific map.

### `start_mapping(client)` / `cancel_mapping(client)` / `save_mapping(client)`

**POST /api/v1/mapping/start**
**POST /api/v1/mapping/cancel**
**POST /api/v1/mapping/save**
Control SLAM mapping.

### `change_map(client, map_data)` / `remap(client)`

**POST /api/v1/mapping/change**
**POST /api/v1/mapping/remap**
Switch or refresh maps.

---

## 📍 Targets

### `get_all_targets(client)`

**GET /api/v1/targets**
List all targets.

### `add_target(client, target_data)`

**POST /api/v1/targets**
Add new named location.

### `get_targets_by_site(client, site)` / `get_targets_by_floor(client, site, floor)`

\*\*GET /api/v1/targets/{site}\`\`
**GET /api/v1/targets/{site}/{floor}**
Filter targets.

### `get_target_by_name(client, site, floor, name)` / `update_target(...)` / `delete_target(...)`

**GET / PATCH / DELETE /api/v1/targets/{site}/{floor}/{name}**
Fetch, edit, or remove a target.

---

## 🛣️ Cruise

### `get_all_cruises(client)` / `get_cruises_by_site(...)` / `get_cruises_by_floor(...)`

**GET /api/v1/cruises**, etc.
List or filter cruise routes.

### `add_cruise(client, cruise_data)` / `update_cruise(...)` / `delete_cruise(...)`

**POST / PATCH / DELETE /api/v1/cruises/{site}/{floor}/{name}**
Manage multi-target patrol routes.

### `get_default_route(client)` / `set_default_route(client, route_data)`

**GET / POST /api/v1/config/default-route**
Control default route.

---

## ✅ Tasks

### `get_all_tasks(client)` / `create_or_update_task(client, data)`

**GET / POST /api/v1/tasks**
List or send tasks (e.g. deliver to table).

### `get_task_by_id(...)` / `update_task(...)` / `delete_task(...)`

**GET / PATCH / DELETE /api/v1/tasks/{task\_uid}**
Manage specific task.

### `pause_task(client)`

**POST /api/v1/task/pause**
Pause active task.

---

## 🖥️ User Interface

### `send_speech_command(client, speech_data)`

**POST /api/v1/ui/speech**
Text-to-speech interaction.

### `set_screen_pixel(client, pixel_data)`

**POST /api/v1/ui/screen/pixel**
Change image or video on the robot screen.

---

## 📦 Python Package Usage Example

```python
from saharobotik.client import SahaRobotikClient
from saharobotik.status import get_robot_status

client = SahaRobotikClient("http://192.168.3.3:7242", api_key="YOUR_API_KEY")
status = get_robot_status(client)
print(status["battery_percent"])
```

This documentation is continually evolving to reflect the latest updates and capabilities of the robot.
