import rclpy
from rclpy.node import Node

import time

class WaitServer(Node):
    def __init__(self):
        super().__init__(self):
        self.get_logger().info('Wait Server Created')
        self._serverName = 'wait'

    def Update(self):
        self.get_logger().info('Wait Server Update')

    def ServerCall(self, data):
        self.get_logger().info('Wait Server Called')
        waitTime = int(data[1])
        time.sleep(self.waitTime)
        msg = 'Waited ' + waitTime + ' seconds'
        return msg
    