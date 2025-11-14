# example_project
* In a terminal:
  1. clone repo
  2. cd into repo
  3. add ROS variables to the terminal's environment
  * `source /opt/ros/jazzy/setup.bash`
  4. build the code:
  * `colcon build`
  5. add this project's variables to the terminal's environment
  * `source install/local_setup.bash`
  6. run the listener node
  * `ros2 run py_pubsub listener`
* In another terminal:
  1. cd into repo
  2. add ROS variables to the terminal's environment
  * `source /opt/ros/jazzy/setup.bash`
  3. add this project's variables to the terminal's environment
  * `source install/local_setup.bash`
  4. run the talker node
  * `ros2 run py_pubsub talker`
* basic ROS talker and listener node source code found in src/py_pubsub/py_pubsub/
* Other example node source code found in src/param_pubsub/param_pubsub/
* Examples of launchfiles & parameters found in src/param_pubsub/launch/
* GPIO example usage found in src/include/
