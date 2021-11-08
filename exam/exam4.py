class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)


def parents(r, data):
    if r == None:
        return 'none because 3 is root!!!'
    else:
        if r.right != None:
            if r.right.data == data:
                return r.data
        if r.left != None:
            if r.left.data == data:
                return r.data
        if data >= r.data:
            return parents(r.right, data)
        else:
            return parents(r.left, data)


tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)
printTree(tree.root)
if data[1] in data[0]:
    print('\nParents of', data[1], 'is', parents(tree.root, data[1]))
else:
    print('\nParents of', data[1], 'is not found!!!')
