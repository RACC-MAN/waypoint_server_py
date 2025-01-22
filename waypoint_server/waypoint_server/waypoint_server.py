import rclpy
from rclpy.node import Node

from waypoint_server_msg.srv import Command

from waypoint_server/wait_server import WaitServer
from waypoint_server/skip_server import SkipServer
from waypoint_server/speak_server import SpeakServer
from waypoint_server/map_change_server import MapChangeServer

class WaypointServer(Node):
    def __init__(self):
        super().__init__('waypoint_server')
        self._server = self.create_service(
            Command,
            'waypoint_command',
            self.callback
        )

        self.wait_server = WaitServer()
        self.skip_server = SkipServer()
        self.speak_server = SpeakServer()
        self.map_change_server = MapChangeServer()
        # self.ex_server = Server()

    
    def callback(self, request, response):
        self.get_logger().info('Accepted command')
        command_line = request.command
        data = command_line.split(',')

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