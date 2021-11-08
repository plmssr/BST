
class Node:

    def __init__(self, data):

        self.data = data

        self.left = None

        self.right = None


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

    def findMin(self, root):
        if root.left != None:
            return self.findMin(root.left)
        else:
            return root.data

    def findMax(self, root):
        if root.right != None:
            return self.findMax(root.right)
        else:
            return root.data

    def printTree(self, node, level=0):

        if node != None:

            self.printTree(node.right, level + 1)

            print('     ' * level, node.data)

            self.printTree(node.left, level + 1)


T = BST()

inp = [int(i) for i in input('Enter Input : ').split()]

for i in inp:

    root = T.insert(i)

T.printTree(root)

print('-' * 50)
print('Min : '+str(T.findMin(root)))
print('Max : '+str(T.findMax(root)))
