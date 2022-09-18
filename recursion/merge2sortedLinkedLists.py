from __Classes import Node

def sortedMerge(A, B):
    if A == None: return B
    if B == None: return A

    if A.name < B.name:
        A.next = sortedMerge(A.next, B)
        return A
    else:
        B.next = sortedMerge(A, B.next)
        return B
    
# Linked List A
A1 = Node(5)
A2 = Node(8)
A3 = Node(22)
A4 = Node(40)
A5 = Node(397)
A1.next = A2
A2.next = A3
A3.next = A4
A4.next = A5
# Linked List B
B1 = Node(4)
B2 = Node(11)
B3 = Node(16)
B4 = Node(333)
B1.next = B2
B2.next = B3
B3.next = B4
# Running of code and print
A1.printList()
B1.printList()
sortedMerge(A1, B1).printList()