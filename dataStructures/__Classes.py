#==========================================================================================
#==========================================================================================
from re import S


class Stack:
    # Create an empty stack or a stack with one element
    def __init__(self, firstEle=None):
        self.n = 0
        self.__list__ = []
        if firstEle:
            self.push(firstEle)
    # Returns amount of elements in stack
    def size(self):
        return len(self.__list__)
    # Checks if stack is empty
    def isEmpty(self):
        return self.size() == 0
    # Adds element to stack
    def push(self, ele):
        return self.__list__.append(ele)
    # Removes element from stack
    # Raises exception if stack is empty
    def pop(self):
        if self.isEmpty():
            raise Exception("Can not pop an empty stack")
        return self.__list__.pop()
    # Look at the top most element without removing it
    # Raises exception if stack is empty
    def peek(self):
        if self.isEmpty():
            raise Exception("There is no element to peak")
        return self.__list__(self.size()-1)
    # Make class iterable
    def __iter__(self):
        return self
    def __next__(self):
        if self.n <= self.size()-1:
            result = self.n
            self.n += 1
            return result
        else:
            raise StopIteration
#==========================================================================================
#==========================================================================================
class Queue:
    def __init__(self, firstEle=None):
        self.n = 0
        self.__list__ = []
        if firstEle:
            self.offer(firstEle)
    # Returns the size of the queue
    def size(self):
        return len(self.__list__)
    # Checks if queue is empty
    def isEmpty(self):
        return self.size() == 0
    # Peeks the element at the front of the queue
    # Raises and exception if the queue is empty
    def peek(self):
        if self.isEmpty():
            raise Exception("Queue Empty")
        return self.__list__(self.size()-1)
    # Poll an element form the front of the queue
    # Raises an exception if the queue is empty
    def poll(self):
        if self.isEmpty():
            raise Exception("Queue Empty")
        return self.__list__.pop(0)
    # Add an element to the back of the queue
    def offer(self, ele):
        self.__list__.append(ele)
    # Make class iterable
    def __iter__(self):
        return self
    def __next__(self):
        if self.n <= self.size()-1:
            result = self.n
            self.n += 1
            return result
        else:
            raise StopIteration