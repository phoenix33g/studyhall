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