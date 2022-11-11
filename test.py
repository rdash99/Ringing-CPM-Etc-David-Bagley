import sys
import time


from node import BellNode

node = BellNode("127.0.0.1", 10002, "Rowan")

time.sleep(1)

# Do not forget to start your node!
node.start()

time.sleep(1)

# Connect with another node, otherwise you do not create any network!
node.connect_with_node('8.tcp.ngrok.io', 12933)
time.sleep(2)

# Example of sending a message to the nodes (dict).
node.send_to_nodes({"message": "Hi there!"})

try:
    while True:
        node.send_to_nodes({"message": "Hello!"})
        time.sleep(0.01)

except KeyboardInterrupt:
    node.stop()
