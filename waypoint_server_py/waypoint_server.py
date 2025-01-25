import rclpy
from rclpy.node import Node

from waypoint_server_msgs.srv import Command

from waypoint_server_py.wait_server import WaitServer
from waypoint_server_py.skip_server import SkipServer
from waypoint_server_py.speak_server import SpeakServer
from waypoint_server_py.map_change_server import MapChangeServer

class WaypointServer(Node):
    def __init__(self):
        super().__init__('waypoint_server')

        self.wait_server = WaitServer()
        self.skip_server = SkipServer()
        self.speak_server = SpeakServer()
        self.map_change_server = MapChangeServer()
        # self.ex_server = Server()

        self._server = self.create_service(
            Command,
            'waypoint_command',
            self.callback
        )

    
    def callback(self, request, response):
        self.get_logger().info('Accepted command')
        command_line = request.command
        data = command_line.split(':')

        # server update, when waypoint updated
        if data[0] == 'update':
            self.Update()
            result_msg = 'All Server Updated'
        # Wait Server call
        elif data[0] == self.wait_server._serverName:
            result_msg = self.wait_server.ServerCall(data)
        # Skip Server call
        elif data[0] == self.skip_server._serverName:
            result_msg = self.skip_server.ServerCall(data)
        # Talk Server call
        elif data[0] == self.speak_server._serverName:
            result_msg = self.speak_server.ServerCall(data)
        # MapChange server call
        elif data[0] == self.map_change_server._serverName:
            result_msg = self.map_change_server.ServerCall(data)
        # # Example server call
        # elif data[0] == self.ex_server._serverName:
        #     result_msg = self.ex_server.ServerCall(data)
        else:
            self.get_logger().warn(f'Wrong command entered : {data[0]}')
            result_msg = "Waypoint Server Faild"


        response.message = result_msg
        return response

    def Update(self):
        self.wait_server.Update()
        self.skip_server.Update()
        self.speak_server.Update()
        self.map_change_server.Update()
        # self.ex_server.Update()



def main(arg=Node):
    rclpy.init()

    node = WaypointServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()