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
                if val >= parent.data:
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

    def checkDuplicate(self, node, value):
        if node is None:
            return 0
        else:
            if node.data <= value:
                return 1 + self.check(node.right, value)+self.check(node.left, value)
            else:
                return 0 + self.check(node.right, value)+self.check(node.left, value)

    def minValueNode(self, node):
        current = node
        while(current.left is not None):
            current = current.left

        return current

    def maxValueNode(self, node):
        current = node
        while(current.right is not None):
            current = current.right
        return current

    def deleteNode(self, root, key):

        # Base Case
        if root is None:
            return print("Error! Not Found DATA")

        if key < root.data:
            root.left = self.deleteNode(root.left, key)

        elif(key > root.data):
            root.right = self.deleteNode(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                self.root = None
                return temp

            elif root.right is None:
                temp = root.left
                self.root = None
                return temp
            # if root have 2 node do this
            temp = self.minValueNode(root.right)

            root.data = temp.data

            root.right = self.deleteNode(root.right, temp.data)

        return root

    def checkType(self, root, key):
        # Base Case
        if root is None:
            return print("Not exist")

        if key < root.data:
            root.left = self.checkType(root.left, key)

        elif(key > root.data):
            root.right = self.checkType(root.right, key)

        else:
            if root.left is None and root.right is None:
                print("Leaf")
                return root
            elif root.left is not None and root.right is not None:
                print("Inner")
                return root
            elif root.left is None:
                print('Inner')
                return root

            elif root.right is None:
                print('Inner')
                return root

        return root


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
num = inp.pop(0)
root = None
for i in inp:
    root = T.insert(i)
T.printTree(root)
if root.data == num:
    print("Root")
else:
    T.checkType(root, num)
