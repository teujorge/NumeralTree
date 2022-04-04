from pydot import Dot, Edge
import uuid
import os.path as op

class Node:
    # constructor
    def __init__(self, data, limit=-1):

        # node variables
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.depth = 0
        self.id = self._id()

        # create left side of tree
        if limit != -1:
            node = self
            for i in range(limit):
                left, right = calc(node.data)
                node._insert(left, right)
                node = left

    # insert Node
    def _insert(self, left, right):
        # left
        self.left = left
        self.left.parent = self
        self.left.depth = self.depth + 1
        # right
        self.right = right
        self.right.parent = self
        self.right.depth = self.depth + 1

    # iterative console print
    def _print(self):

        # assume good
        r = True

        # left
        if self.left:
            r = self.left._print()

        # condition
        print(self.data)

        # right
        if self.right:
            r = self.right._print()

        # status
        return r

    # iterative pydot tree drawing
    def _draw(self, graph: Dot):

        # left
        if self.left:
            self.left._draw(graph)

        # add edges
        try:
            edge = Edge(str(self.parent.id) + "\n" + str(self.parent.data), str(self.id) + "\n" + str(self.data))
            graph.add_edge(edge)
        # NoneType expected at ends of trees
        except AttributeError:
            pass

        # right
        if self.right:
            self.right._draw(graph)

    # iterative fill tree using logic
    def _fill(self, depth: int):

        # assume good
        r = True

        # left
        if self.left:
            r = self.left._fill(depth)

        # condition
        if self.left == None or self.right == None:
            if self.depth < depth:
                left, right = calc(self.data)
                self._insert(left, right)
                return False

        # right
        if self.right:
            r = self.right._fill(depth)

        # status
        return r

    # unique id for each node
    def _id(self):
        id1 = uuid.uuid4()
        id2 = uuid.uuid4()
        # shortened id (better looking)
        return "#" + id1.hex[1:4] + id2.hex[6:10]

# class Node


# obtain init input
def get_input(label):
    num = -1
    while not num >= 0:
        try:
            num = int(input(label + ": "))
        except Exception as e:
            print(e)
    return num

# tree logic
def calc(number):
    # add 1 if odd
    if number % 2 != 0:
        number = int(number+1)
    # logic
    number1 = int(((100+number)/2) % 100)
    number2 = int((number/2) % 100)
    return Node(number1), Node(number2)

# run
def main():
    # obtain inputs
    depth = get_input("depth")
    number = get_input("number")
    
    # init
    root = Node(number, depth)
    graph = Dot(graph_type='digraph')

    # generate tree w/ calc logic
    while not root._fill(depth):
        pass

    # generate graph w/ pydot module
    root._draw(graph)

    # generate file (no overwriting)
    count = 1
    fname = "graph" + str(count) + ".png"
    while op.isfile(fname):
        count += 1
        fname = "graph" + str(count) + ".png"
    graph.write_png(fname)

    # print tree
    root._print()

# program
if __name__ == "__main__":
    main()