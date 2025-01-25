import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class SpeakServer(Node):
    def __init__(self):
        super().__init__(self):
        self.get_logger().info('Speak Server Created')
        self._serverName = 'speak'

    def Update(self):
        self.get_logger().info('Speak Server Update')

    def ServerCall(self, data):
        self.get_logger().info('Speak Server Called')
        #---------------------------------
        # Write speak procss with data[1]
        #---------------------------------
        msg = 'Speak Server Accepted'
        return msg
