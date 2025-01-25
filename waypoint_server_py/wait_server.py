import rclpy
from rclpy.node import Node

import time

class WaitServer(Node):
    def __init__(self):
        super().__init__('wait_server')
        self.get_logger().info('Wait Server Created')
        self._serverName = 'wait'

    def Update(self):
        # self.get_logger().info('Wait Server Update')
        pass

    def ServerCall(self, data):
        self.get_logger().info(f'Wait Server Called, wait for {data[1]} seconds')
        waitTime = int(data[1])
        time.sleep(waitTime)
        self.get_logger().info(f'Finish waiting')
        msg = 'Waited ' + data[1] + ' seconds'
        return msg
    