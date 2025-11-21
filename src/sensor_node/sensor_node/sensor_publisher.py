import rclpy                    # import the ROS Client Library for Python (RCLPY)
from rclpy.node import Node     # from RCLPY, import the Node Class used to create ROS 2 nodes
from std_msgs.msg import String # from standard messages, import the String message
from std_msgs.msg import Int32

import os
include_dir = os.path.dirname(os.path.realpath(__file__)) + "/../../../../../../src/include/"
import sys
sys.path.append(include_dir)
from hat_library import *

class MinimalPublisher(Node):   # Create a new class called MinimalPublisher that inherits variables & functions from Node

    def __init__(self):
        super().__init__('minimal_publisher')                               # Initialize the Node with the name 'minimal_publisher'
        self.publisher_ = self.create_publisher(Int32, 'sensor_readings', 10)  # Create a publisher for String type messages on the topic 'my_topic'
        self.declare_parameter('publish_rate', 1)                        # Instantiate parameter, set default value to 'Hi'
        publish_rate = self.get_parameter('publish_rate').get_parameter_value().integer_value
        timer_period = publish_rate                                                  # Define the timer period in seconds
        self.declare_parameter('sensor_num', 1)  
        self.timer = self.create_timer(timer_period, self.timer_callback)   # Create a timer that calls 'timer_callback' every 0.5 seconds

    def timer_callback(self):                
        sensor_num = self.get_parameter('sensor_num').get_parameter_value().integer_value
        if(sensor_num == 1):
            self.irValue = get_ir_state(IR1_INPUT_PIN)
        if(sensor_num == 2):
            self.irValue = get_ir_state(IR2_INPUT_PIN)
        msg = Int32()
        msg.data = self.irValue
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):
    print ("Beginning to talk...")          # Print a starting message
    rclpy.init(args=args)                   # Initialize the ROS 2 Python client library

    minimal_publisher = MinimalPublisher()  # Create an instance of the MinimalPublisher class

    try:
        rclpy.spin(minimal_publisher)       # Keep the node active and processing callbacks until interrupted

    except KeyboardInterrupt:   # Handle a keyboard interrupt (Ctrl+C)
        print("\n")             # Print a newline for better format
        print("Stopping...")    # Print a stopping message
 
    finally:
        # Destroy the node explicitly
        # (optional - otherwise it will be done automatically
        # when the garbage collector destroys the node object)
        minimal_publisher.destroy_node()
        if rclpy.ok():                      # Check if the rclpy library is still running
            rclpy.shutdown()                # Shut down the ROS 2 client library, cleanly terminating the node



if __name__ == '__main__':
    main()                  # Call the main function to execute the code when the script is run