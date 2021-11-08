class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val, root=None):
        if root is None:
            self.root = Node(val)
            return self.root

        else:
            if root.data <= val:
                root.right = self.insert(val, root.right)
            else:
                root.left = self.insert(val, root.left)

    def insertIt(self, val):
        while self.data != None:
            if val >= self.data:
                self.data = self.right
            elif val < self.data:
                self.data = self.left

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
root = T.insert(inp[0])
print(T.root)
for i in inp:
    print(root)
    root = T.insert(i, root)

T.printTree(root)
