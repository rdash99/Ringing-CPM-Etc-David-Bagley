from node import BellNode
import sys
import time
import serial.tools.list_ports as serial


def calibrate():
    nodes = []

    MainNode = BellNode("127.0.0.1", 10001, "main", True)
    port = 10002

    ports = serial.comports()

    for SerialPort in ports:
        print(SerialPort.name)
        nodes.append(BellNode("127.0.0.1", port,
                     "Port " + str(SerialPort.name), True))
        port += 1

    print("Generated " + str(len(nodes)) + " nodes.")

    for node in nodes:
        node.start()
        MainNode.connect_with_node(node.host, node.port)
        node.send_to_nodes(data={"message": "Hi there!"})
    time.sleep(1)

    MainNode.send_to_nodes({"message": "Hi there!"})
    MainNode.stop()

    for node in nodes:
        node.stop()


calibrate()
"""Scan all connected serial ports and create a node for each one to allow for calibrarion of which bell is which port."""
