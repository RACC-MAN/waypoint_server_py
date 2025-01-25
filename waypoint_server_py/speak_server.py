import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class SpeakServer(Node):
    def __init__(self):
        super().__init__('speak_server')
        self.get_logger().info('Speak Server Created')
        self._serverName = 'speak'

    def Update(self):
        # self.get_logger().info('Speak Server Update')
        pass

    def ServerCall(self, data):
        self.get_logger().info(f'Speak Server Called, msg : {data[1]}')
        #---------------------------------
        # Write speak procss with data[1]
        #---------------------------------
        msg = 'Speak Server Accepted'
        return msg
