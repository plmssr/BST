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

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return self.root
        else:
            cur = self.root
            while cur != None:
                parent = cur
                if val >= cur.data:
                    cur = cur.right
                else:
                    cur = cur.left
            if val >= parent.data:
                parent.right = Node(val)
            else:
                parent.left = Node(val)
            return self.root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def deep(self, node, level=0, max=0):
        if node is None:
            return max
        else:
            if level > max:
                max = level
            righ = self.deep(node.right, level + 1, max)
            left = self.deep(node.left, level + 1, max)
            if righ >= left and righ > max:
                max = righ
            elif left >= righ and left > max:
                max = left
            return max


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print('Height of this tree is : '+str(T.deep(root)))
