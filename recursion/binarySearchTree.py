from __Classes import BinaryNode

def insertNode(head, data):
    if head == None:
        head = BinaryNode(data)
        return head
    if head.data < data:
        head.right = insertNode(head.right, data)
    else:
        head.left = insertNode(head.left, data)
    return head



import random

b = BinaryNode(50)
for _ in range(50):
    insertNode(b, random.randint(0, 100))
b.printTree()
b.right.left.right.printTree()