class Node:
        def __init__(self, data, next=None):
            self.data = data
            if next is None:
                self.next = None
            else:
                self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.isLoop = False

    def __str__(self):
        if len(self) == 0:
            return 'Empty'
        else :
            s = ''
            p = self.head
            while p is not None:
                s += str(p.data)
                p = p.next
                if p is not None:
                    s+= '->'
            return s

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def indexOf(self, data):
        q = self.head
        for i in range(len(self)):
            if q.data == data:
                return i
            q = q.next
        return -1

    def isIn(self, data):
        return self.indexOf(data) >= 0

    def nodeAt(self, i):
        p = self.head
        for j in range(0, i):
            p = p.next
        return p

    def append(self, data):
        if self.head is None:
            self.head = self.Node(data, None)
            self.size += 1
        else:
            self.insertAfter(self.size - 1, data)

    def insertAfter(self,i,data) :   
        i = int(i)
        if i == -1:
            p = self.Node(data)
            p.next = self.head
            self.head = p
        else:
            q = self.nodeAt(i)
            p = self.Node(data)
            p.next = q.next
            q.next = p
        self.size += 1

    def deleteAfter(self, i): 
        i = int(i)
        if self.size > 0:
            p = self.nodeAt(i)
            p.next = p.next.next
            self.size -= 1

    def delete(self,i) :
        i = int(i)
        if i == 0 and self.size > 0 :           
          self.head = self.head.next
          self.size -= 1
        else :
          self.deleteAfter(i-1)  

    def set_next(self, index1, index2):
        index1 = int(index1)
        index2 = int(index2)
        if len(self) == 0:
            print('Error! {list is empty}')
        elif index1 >= len(self):
            print('Error! {index not in length}: '+ str(index1))
        elif index2 >= len(self):
            print(f'index not in length, append : {index2}')
            self.append(index2)
        else:
            print('Set node.next complete!, index:value = ',end='')
            p = self.nodeAt(index1)
            q = self.nodeAt(index2)
            print(f'{index1}:{str(p.data)} -> {index2}:{str(q.data)}')
            if index2 <= index1:
                self.isLoop = True
            else:
                p.next = q
                self.size -= (index2 - index1) - 1

    def checkLoop(self):
        if self.isLoop:
            print('Found Loop')
        else:
            print('No Loop')
            print(self)

input = [e for e in input("Enter input : ").split(',')]

L = LinkedList()

for i in input:
    command, Data = i.split(' ')
    Data = str(Data)
    if command == 'A':
        L.append(Data)
        print(L)
    else:
        L1, L2 = Data.split(':')
        L.set_next(L1,L2)

L.checkLoop()