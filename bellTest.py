from node import BellNode
import sys
import time

bellNum = 12

nodes = []

MainNode = BellNode("127.0.0.1", 10001, "main")
port = 10002
for i in range(bellNum):
    nodes.append(BellNode("127.0.0.1", port, "Bell " + str(i+1)))
    port += 1
print("Generated " + str(len(nodes)) + " nodes.")
time.sleep(1)
MainNode.start()
# Do not forget to start your node!

for node in nodes:
    node.start()
    MainNode.connect_with_node("127.0.0.1", node.port)
time.sleep(1)

# Connect with another node, otherwise you do not create any network!
time.sleep(2)

# Example of sending a message to the nodes (dict).
MainNode.send_to_nodes({"message": "Hi there!"})

time.sleep(5)  # Create here your main loop of the application

MainNode.stop()
for node in nodes:
    node.send_to_nodes({"message": "Bye!"})
    node.stop()
