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

# Binary Node: for Binary search trees
class BinaryNode():
    def __init__(self, data):
        self.data = data
        self.__left = None
        self.__right = None
    @property
    def left(self):
        return self.__left
    @left.setter
    def left(self, node):
        self.__left = node
    @property
    def right(self):
        return self.__right
    @right.setter
    def right(self, node):
        self.__right = node

    def insertNode(self, data):
        if self == None:
            self = BinaryNode(data)
            return
        if self.data == data:
            return
        if self.data < data:
            if self.right == None:
                self.right = BinaryNode(data)
                return
            self.right.insertNode(data)
        else:
            if self.left == None:
                self.left = BinaryNode(data)
                return
            self.left.insertNode(data)

    def printTree(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


# Node Graph
class GraphNode():
    def __init__(self, data):
        self.data = data
        self.__neighbors = []
    def getNeighbors(self):
        return self.__neighbors
    def addNeighbor(self, node):
        self.__neighbors.append(node)