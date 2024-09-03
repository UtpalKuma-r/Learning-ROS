#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class node_class(Node):
    def __init__(self):
        super().__init__("node_name_1")
        self.iter = 0
        # self.get_logger().info("Node created")
        self.create_timer(1, self.callback_function)
        


    def callback_function(self):
        self.get_logger().info("Line" + str(self.iter))
        self.iter += 1

def main(args=None):
    rclpy.init(args=args)
    node = node_class()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()