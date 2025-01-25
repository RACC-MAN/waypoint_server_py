import rclpy
from rclpy.node import Node

class MapChangeServer(Node):
    def __init__(self):
        super().__init__('map_change_server')
        self.get_logger().info('Map Change Server Created')
        self._serverName = 'map_change'

    def Update(self):
        # self.get_logger().info('Map Change Server Update')
        pass

    def ServerCall(self, data):
        self.get_logger().info(f'Map Change Server Called, path : {data[1]}')
        #--------------------------
        # Write map change process
        #--------------------------
        msg = 'Map Change Completed'
        return msg