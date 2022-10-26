class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def pushTail(self,data):
        curr = self.head
        n = Node(data)
        if curr is None:
            self.head = n
            return

        if curr.data > data:
            n.next = curr
            self.head = n
            return

        while curr.next is not None:
            if curr.data < data and curr.next.data > data:
                break
            curr = curr.next
        n.next = curr.next
        curr.next = n

    def popHead(self):
        self.head = self.head.next

    def popTail(self):
        newNode = self
        if self.head is None:
            self = newNode
            return
        node = self.head
        while node.next.next:
            node = node.next
        node.next = None

    def size(self):
        node = self.head
        len = 0
        while node != None:
            len += 1
            node = node.next
        return len

    def isEmpty(self):
        return self.head == None

    def __str__(self):
        node = self.head
        s = ''
        while node != None:
            s += str(node.data)
            if node.next != None:
                s += ' '
            node = node.next
        return s
    
    def isIn(self,data):
        node = self.head
        while node != None:
            if node == data:
                return True
            node = node.next
        return False          

inp = input('Enter Input : ').split()
bef = []
li = []
num = [LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList()]
digit = 0
size = len(inp)
keep = False
while num[0].size() != size:
    digit += 1
    for i in inp:
        if not keep:
            bef.append(i)
        temp = int(i)
        if temp < 0:
            temp *= -1
            temp = int(((temp - (int(i)*-1) % (pow(10,digit-1)))/pow(10,digit-1))%10)
        else:
            temp = int(((temp - int(i) % (pow(10,digit-1)))/pow(10,digit-1))%10)
        num[temp].pushTail(int(i))
        if temp == 0:
            li.append(i)
    keep = True
    for i in li:
        inp.remove(i)
    li = []
    print('------------------------------------------------------------')
    print('Round :',str(digit))
    print('0 :',num[0])
    for i in range(1,len(num)):
        print(i,':',num[i])
        num[i] = LinkedList()

print('------------------------------------------------------------')
print(str(digit-1),'Time(s)')
print('Before Radix Sort :',' -> '.join(bef))
print('After  Radix Sort :',' -> '.join(str(num[0]).split()))