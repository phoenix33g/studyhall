from __Classes import BinaryNode
import random

UGLY = ''

def allLeavesString(head):
    global UGLY
    if head is None: return
    if head.left is None and head.right is None: UGLY += f"[{head.data}]"
    if head.left is not None:
        allLeavesString(head.left)
    if head.right is not None:
        allLeavesString(head.right)

# Create a random Binary tree for testing
b = BinaryNode(50)
for _ in range(50):
    b.insertNode(random.randint(0, 100))
b.printTree()
print("--------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------")
# Print all leaves of random Binary tree
allLeavesString(b)
print(UGLY)