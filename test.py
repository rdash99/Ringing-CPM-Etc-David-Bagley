import sys
import time

from node import BellNode

node = BellNode("127.0.0.1", 10001)
node2 = BellNode("127.0.0.1", 10002)
time.sleep(1)

# Do not forget to start your node!
node.start()
node2.start()
time.sleep(1)

# Connect with another node, otherwise you do not create any network!
node.connect_with_node('127.0.0.1', 10002)
time.sleep(2)

# Example of sending a message to the nodes (dict).
node.send_to_nodes({"message": "Hi there!"})

time.sleep(5)  # Create here your main loop of the application

node.stop()
node2.stop()
