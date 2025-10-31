# Saha SDK Python

Official Python SDK for Saha Robotik API - A comprehensive library for interacting with the Saha Robotik platform.

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 🚀 Features

- **Easy Installation**: Install with a single command
- **Comprehensive API Support**: Supports all Saha Robotik API endpoints
- **Type Hints**: Full IDE support with Python type hints
- **Pydantic Models**: Safe data validation
- **Error Handling**: Detailed error management
- **Well Documented**: Extensive documentation and examples

## 📋 Supported API Modules

- ✅ **Navigation**: Robot navigation, positioning, goal setting
- ✅ **Status**: Robot status, battery, hardware monitoring
- ✅ **Targets**: Target creation, update, deletion
- ✅ **Tasks**: Task management
- ✅ **Cruise**: Patrol routes
- ✅ **Mapping**: Map management
- ✅ **Layers**: Layer management
- ✅ **Profile**: Robot profiles and modes
- ✅ **UI**: Speech and screen control

## 📦 Installation

### Install from PyPI

```bash
pip install saha-sdk
```

### Install for Development

```bash
git clone https://github.com/saharobotik/saha-sdk-python.git
cd saha-sdk-python
pip install -e .
```

## 🎯 Quick Start

### Basic Usage

```python
from saha_sdk.client import Robot
from saha_sdk import status, navigation

# Create robot client
robot = Robot("http://192.168.1.100:5000")

# Optional: Add API key if required
# robot.set_api_key("your-api-key")

# Check robot status
robot_status = status.get_robot_status(robot)
print(f"Battery: {robot_status.battery_percent}%")
print(f"State: {robot_status.current_state}")

# Get position
position = navigation.get_current_position(robot)
print(f"Position: x={position.position.x}, y={position.position.y}")
```

### Navigate to Target

```python
from saha_sdk import navigation
from saha_sdk.models import Position

# Navigate using target UID
navigation.set_goal_target(robot, "site_floor_target_01")

# Or navigate using coordinates
target_position = Position(x=5.0, y=3.0, theta=1.57)
navigation.set_goal_pose(robot, target_position)
```

### Make Robot Speak

```python
from saha_sdk import ui
from saha_sdk.models import SpeechModel

speech = SpeechModel(
    lang="en",  # English
    text="Hello! I am Saha Robot."
)

ui.speak_text(robot, speech)
```

## 📚 Detailed Examples

Find working examples in the `examples/` directory:

| Example | Description |
|---------|-------------|
| `01_basic_connection.py` | Basic connection and status check |
| `02_go_to_target_and_speak.py` | Navigate to target and say "Hello World" |
| `03_list_targets.py` | List all targets |
| `04_start_cruise.py` | Start a patrol route |
| `05_emergency_stop.py` | Emergency stop |
| `06_check_hardware.py` | Hardware status check |

```bash
cd examples
python 02_go_to_target_and_speak.py
```

## 🔧 API Modules

### Navigation

```python
from saha_sdk import navigation
from saha_sdk.models import Position, TwistModel, RobotStopModel, SiteFloorModel

# Get position
position = navigation.get_current_position(robot)
path = navigation.get_navigation_path(robot)

# Navigate to target
navigation.set_goal_target(robot, "target_uid")
navigation.set_goal_pose(robot, Position(x=1.0, y=2.0, theta=0.5))

# Velocity control
navigation.send_safe_velocity(robot, TwistModel(vel_x=0.5, vel_z=0.0))

# Emergency stop
navigation.set_emergency_stop(robot, RobotStopModel(stop=True))

# Localization
navigation.start_localization(robot, SiteFloorModel(site="site1", floor="floor1"))
```

### Status

```python
from saha_sdk import status

# General status
robot_status = status.get_robot_status(robot)

# Hardware status
hw_status = status.get_hardware_status(robot)

# Robot information
info = status.get_robot_info(robot)
```

### Targets

```python
from saha_sdk import targets
from saha_sdk.models import TargetRequestModel

# List targets
all_targets = targets.get_all_targets(robot)
site_targets = targets.get_targets_by_site(robot, "site1")

# Add/update/delete targets
target = TargetRequestModel(
    name="new_target", site="site1", floor="floor1",
    eg="", eg_dir="", px=5.0, py=3.0, yaw_deg=90.0
)
targets.add_target(robot, target)
targets.update_target(robot, "site1", "floor1", "target_name", target)
targets.delete_target(robot, "site1", "floor1", "target_name")
```

### Tasks

```python
from saha_sdk import task
from saha_sdk.models import TaskRequestModel

# Task management
all_tasks = task.get_all_tasks(robot)
task.create_task(robot, TaskRequestModel(
    type="TABLE_SERVICE", activate=True,
    target_uid="target_01", payload=[False, False, False, False]
))

# Task control
task.pause_mission(robot)
task.resume_mission(robot)
task.clear_all_tasks(robot)
```

### Cruise

```python
from saha_sdk import cruise
from saha_sdk.models import CruiseRequestModel, CruiseControlRequestModel

# Cruise management
all_cruises = cruise.get_all_cruises(robot)
cruise.add_cruise(robot, CruiseRequestModel(
    name="patrol_1", site="site1", floor="floor1",
    waypoints=["target1", "target2", "target3"]
))

# Start cruise
cruise.start_cruise(robot, CruiseControlRequestModel(
    cruise_cmd="CMD_START", cruise_route="patrol_1", number_of_rounds=2
))
```

### Mapping

```python
from saha_sdk import mapping
from saha_sdk.models import SiteFloorModel, MappingModel

# Map management
available_maps = mapping.get_available_maps(robot)
current_map = mapping.get_current_map(robot)

# Change map
mapping.change_map(robot, SiteFloorModel(site="site1", floor="floor1"))

# Mapping operations
mapping.start_mapping(robot, MappingModel(
    site_floor=SiteFloorModel(site="site1", floor="floor1"),
    title="new_map"
))
mapping.save_map(robot)
```

### Profile

```python
from saha_sdk import profile
from saha_sdk.models import RobotProfileModel, RobotModeModel

# Profile management
profiles = profile.get_robot_profiles(robot)
profile.change_speed_profile(robot, RobotProfileModel(profile="fast"))
profile.change_behavior_profile(robot, RobotProfileModel(profile="cautious"))

# Mode management
modes = profile.get_robot_modes(robot)
profile.set_robot_mode(robot, RobotModeModel(mode="patrol"))
```

### UI (User Interface)

```python
from saha_sdk import ui
from saha_sdk.models import SpeechModel

# Speech
ui.speak_text(robot, SpeechModel(lang="en", text="Hello!"))

# Screen control
ui.change_pixel_screen_video(robot, "https://example.com/video.mp4")
```

## 🧪 Testing

### Unit Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Generate coverage report
python -m pytest tests/ --cov=saha_sdk --cov-report=html

# Run specific module tests
python -m pytest tests/test_navigation.py -v
```

### Testing with Mock Server

Test without a real robot:

```bash
# Terminal 1: Start mock server
cd examples
pip install flask
python mock_robot_server.py

# Terminal 2: Run example
python 02_go_to_target_and_speak.py
```

## 🐛 Error Handling

```python
from saha_sdk.exceptions import (
    SahaRobotikAPIError,
    BadRequestError,
    UnauthorizedError,
    NotFoundError,
    ServerError
)

try:
    result = navigation.set_goal_target(robot, "invalid_target")
except NotFoundError as e:
    print(f"Target not found: {e}")
except UnauthorizedError as e:
    print(f"Authorization error: {e}")
except SahaRobotikAPIError as e:
    print(f"API error: {e}")
```

## 🔐 API Key Management

```python
# Optional: At initialization
robot = Robot("http://robot-ip:port", api_key="your-key")

# Optional: Set later
robot = Robot("http://robot-ip:port")
robot.set_api_key("your-key")
```

## 🛠️ Development

### Requirements

```bash
pip install -e ".[dev]"
```

### Code Quality

```bash
# Format code
black saha_sdk tests examples

# Lint
flake8 saha_sdk tests

# Type checking
mypy saha_sdk
```

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Changelog

### v0.1.0 (2024-10-31)
- Initial release
- Full API endpoint support
- Comprehensive test coverage (100%)
- Examples and documentation

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/saharobotik/saha-sdk-python/issues)
- **Email**: support@saharobotik.com
- **Documentation**: [API Docs](https://api.saharobotik.com/docs)

## 👥 Authors

Saha Robotik Team

---

**Manage your robots with Saha Robotik!** 🤖
