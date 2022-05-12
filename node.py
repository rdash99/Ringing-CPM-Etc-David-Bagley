from p2pnetwork.node import Node
from p2pnetwork.nodeconnection import NodeConnection
import serial


class BellNode (Node):
    last_message = None
    serialPort = None
    serialConnection = None
    callibrationMode = False
    # Python class constructor

    def __init__(self, host, port, id, callibrationMode=False, callback=None, max_connections=0):
        super(BellNode, self).__init__(
            host, port, id, callback, max_connections)
        self.callibrationMode = callibrationMode

    def outbound_node_connected(self, connected_node):
        print("outbound_node_connected: " + connected_node.id)

    def inbound_node_connected(self, connected_node):
        print("inbound_node_connected: " + connected_node.id)

    def inbound_node_disconnected(self, connected_node):
        print("inbound_node_disconnected: " + connected_node.id)

    def outbound_node_disconnected(self, connected_node):
        print("outbound_node_disconnected: " + connected_node.id)

    def node_message(self, connected_node, data):
        print("node_message from " + connected_node.id + ": " + str(data))
        last_message = data

    def node_disconnect_with_outbound_node(self, connected_node):
        print("node wants to disconnect with other outbound node: " + connected_node.id)

    def node_request_to_stop(self):
        print("node is requested to stop!")

    def create_new_connection(self, connection, id, host, port):
        return NodeConnection(self, connection, id, host, port)
