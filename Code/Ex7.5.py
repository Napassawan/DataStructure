Found = False

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

    def insert(self,node):
        if self.root is None:
            self.root= node
        else:
            Rootnode=self.root
            while True:
                if node.data >= Rootnode.data:
                    if Rootnode.right is None :

                        Rootnode.right = node
                        break
                    Rootnode = Rootnode.right
                else:
                    if Rootnode.left is None:
                        Rootnode.left = node
                        break
                    Rootnode = Rootnode.left
    
    def PrintTree(self):
        def _PrintTree(node, level):
            if node != None:
                _PrintTree(node.right, level + 1)
                print('     ' * level, node)
                _PrintTree(node.left, level + 1)
        _PrintTree(self.root, 0)
    
    def checkpos(self,inp):
        global Found
        if inp == self.root.data:
            print('Root')
            return
        def _checkpos(node):
            global Found
            if node != None:
                if node.data != inp:
                    _checkpos(node.left)
                    _checkpos(node.right)
                elif node.data == inp and node.right is None and node.left is None:
                    print('Leaf')
                    Found = True
                elif node.data == inp:
                    print('Inner')
                    Found = True
        _checkpos(self.root)
        if Found == False:
            print('Not exist')
            return

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(Node(inp[i]))
T.PrintTree()
T.checkpos(inp[0])