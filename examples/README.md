# Saha SDK Python - Examples

This folder contains examples demonstrating basic usage of the Saha Robotik SDK.

## Prerequisites

```bash
# Install the SDK
pip install -e ..

# or from PyPI (after release):
# pip install saha-sdk
```

## Examples

### 1. Basic Connection (`01_basic_connection.py`)
Shows how to connect to the robot and retrieve basic status information.

```bash
python 01_basic_connection.py
```

**What it does:**
- Creates a robot client
- Checks robot status
- Displays battery level and robot information

---

### 2. Go to Target and Speak (`02_go_to_target_and_speak.py`)
Sends the robot to a target and makes it say "Hello World" when it arrives.

```bash
python 02_go_to_target_and_speak.py
```

**What it does:**
1. Retrieves the robot's current position
2. Sends a command to go to the specified target
3. Waits until the robot reaches the target
4. Says "Hello World!" upon arrival

**Note:** Replace the `TARGET_NAME` variable with the name of your own target.

---

### 3. List Targets (`03_list_targets.py`)
Lists all saved targets and shows their details.

```bash
python 03_list_targets.py
```

**What it does:**
- Lists all targets
- Shows details of each target (position, type, etc.)
- Example of site-based filtering

---

### 4. Start Cruise (`04_start_cruise.py`)
Demonstrates starting a patrol route (cruise) on the robot.

```bash
python 04_start_cruise.py
```

**What it does:**
- Lists existing cruises
- Checks the default route
- Starts a cruise

---

### 5. Emergency Stop (`05_emergency_stop.py`)
Shows how to stop the robot immediately.

```bash
python 05_emergency_stop.py
```

**What it does:**
- Checks emergency stop status
- Activates emergency stop
- Shows how to resume

---

### 6. Hardware Check (`06_check_hardware.py`)
Checks the status of the robot's hardware components.

```bash
python 06_check_hardware.py
```

**What it does:**
- Checks LIDAR sensors
- Checks cameras
- Checks internet connectivity

---

## Usage Notes

### Robot IP Address
All examples use the default IP address `http://192.168.1.100:5000`.
To use your own robot IP address, change the following line at the top of each example:

```python
robot = Robot("http://192.168.1.100:5000")  # Replace with your own IP
```

### API Key
If your API requires authentication:

```python
robot = Robot("http://192.168.1.100:5000")
robot.set_api_key("your-api-key-here")
```

### Troubleshooting
If an example does not work:
1. Make sure the robot IP address is correct
2. Check that the robot is running
3. Verify network connectivity

### Customization
You can customize each example according to your needs:
- Change target names
- Update speech texts
- Adjust waiting times
- Add new features

## Help

For more information:
- Main documentation: [../README.md](../README.md)
- API Reference: [Saha Robotik API Docs](https://api.saharobotik.com/docs)

## Contributing

If you want to add new examples, feel free to open a pull request!
