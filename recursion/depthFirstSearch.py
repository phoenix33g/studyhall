from __Classes import GraphNode
import random

def depthFirstSearch(head, visitedList, goal):
    if head is None: return False
    if head.data == goal: return True
    for neighbor in head.getNeighbors():
        if neighbor in visitedList: continue
        visitedList.append(neighbor)
        if depthFirstSearch(neighbor, visitedList, goal): return True
    return False

# Create Random Graph of data possibly from 0-100
def createDepthGraph(root, amount, count):
    if count >= amount: return
    if root is None:
        root = GraphNode(random.randint(0,100))
        count += 1
    if len(root.getNeighbors()):
        if not random.randint(0,3):
            # Move to an exsiting Neighbor
            for _ in range(random.randint(1,3)):
                n = root.getNeighbors()
                root = n[random.randint(1,count)%len(n)]
    # Create new neighbor node and move to it
    newNode = GraphNode(random.randint(0,100))
    count += 1
    root.addNeighbor(newNode)
    print(newNode.data)
    createDepthGraph(newNode, amount, count)

# Create graph and output
g = GraphNode(5)
print(5)
createDepthGraph(g, 50, 1)
# Run meat and potatos
searchFor = 33
print(f"Is {searchFor} in the graph? {depthFirstSearch(g, [], searchFor)}")