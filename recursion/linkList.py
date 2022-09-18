# Node class with all the bells and whistles
class Node:
    def __init__(self, name):
        self.name = name
        self.__next = None
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, node):
        self.__next = node

    def printList(self):
        tmp = self
        nameArr = []
        while tmp != None:
            nameArr.append(tmp.name)
            tmp = tmp.next
        print("->".join(str(_name) for _name in nameArr))


# Actual meat and potatos   
def reverseList(head):
    if head == None or head.next == None: return head
    p = reverseList(head.next)
    head.next.next = head
    head.next = None
    return p


# Main setup and running of code
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

n1.printList()
reverseList(n1).printList()