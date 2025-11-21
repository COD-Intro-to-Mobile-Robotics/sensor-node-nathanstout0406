source /opt/ros/jazzy/setup.bash
colcon build
source install/local_setup.bash
ros2 launch src/sensor_node/launch/sensor_node_launchfile.xml