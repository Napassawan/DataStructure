class BST:
    def __init__(self):
        self.root = None
    def setRoot(self,node):
        self.root = node
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        elif self.root != None:
            p=self.root
            found=False
            while not found:
                if p.left == None:
                    p.left=Node(data)
                    found=True
                elif p.right == None:
                    p.right = Node(data)
                    found=True
                elif p.left.left != None and p.left.right != None:
                    p=p.right
                else:
                    p=p.left
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

k,book = input('Enter Input : ').split('/')
book = [int(e) for e in book.split(' ')]
van = {}
for i in range(int(k)):
    van.update({i+1:0})
index=1
while len(book) > 0:
    T=BST()
    van = dict(sorted(van.items(),key= lambda x : x[::-1]))
    for i in van.items():
        T.insert(list(i))
    T.root.data[1]+=book[0]
    van[T.root.data[0]]+=book[0]
    print('Customer {0} Booking Van {1} | {2} day(s)'.format(index,T.root.data[0],book[0]))
    book.pop(0)
    index+=1