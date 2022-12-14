#BST
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self,data,node):
        if data >= node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                node.right.insert(data, node.right)
        elif data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                node.left.insert(data, node.left)

    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.insert(data,self.root)
        return self.root

    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)