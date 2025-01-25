import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped
from sensor_msgs.msg import LaserScan
from example_interfaces.msg import Empty
from visualization_msgs.msg import Marker, MarkerArray

import math

class SkipServer(Node):
    def __init__(self):
        super().__init__('skip_server')
        self.get_logger().info('Skip Server Created')

        self._serverName = 'skip'
        self._skipAvailable = False
        self.skip_tolerance = 0.0

        self._cancelCall = self.create_publisher(Empty, "nav2_cancel", 10)

    def Update(self):
        # self.get_logger().info('Skip Server Update')
        self.skipEnable = False

    def ServerCall(self, data):
        self.get_logger().info('Skip Server Called')
        self._skipAvailable = True
        msg = 'Skip Server Accepted'
        return msg

    def SkipJadge(self):
        self.get_logger().warn('Skip Jadge')
        # if self._skipAvailable:
            #--------------------------
            # Write skip jedge process 
            #--------------------------
            # self._skipAvailable = False
            # self._cancelCall.publish()

