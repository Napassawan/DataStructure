class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.head is None:
            self.head = self.Node(item)
            self.size += 1
        else:
            p = self.head
            for i in range(0,self.size-1):
                p = p.next
            q = self.Node(item)
            p.next = q
            self.size += 1

    def appendNode(self,node):
        p = self.head
        for i in range(0,self.size-1):
            p = p.next
        p.next = node
        self.size += 1

    def addHead(self, item):
        if self.isEmpty():
            p = self.Node(item)
            self.head = p
            self.size += 1
        else:
            p = self.Node(item)
            p.next = self.head
            self.head = p
            self.size += 1

    def search(self, item):
        if self.index(item)>=0:
            return "Found"
        else:
            return "Not Found"

    def index(self, item):
        p=self.head
        for i in range(self.size()):
            if p.value == item:
                return i
            p = p.next
        return -1

    def size(self):
        return self.size

    def pop(self, pos):
        if pos < 0 or pos >= self.size:
            return "Out of Range"
        if pos == 0 and self.size > 0:
            self.head = self.head.next
            self.size -= 1
            return "Success"
        else:
            p = self.head
            for i in range(0,pos-1):
                p = p.next 
            p.next =p.next.next
            self.size -= 1
            return "Success"
    
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
 
    def returnhead(self):
        return self.head


L = LinkedList()
L1, L2 = input('Enter Input (L1,L2) : ').split()
L1, L2 = L1.split('->') , L2.split('->')
list1 = LinkedList()
list2 = LinkedList()
for i in L1:
    list1.append(i)

for i in L2 :
    list2.append(i)

print('L1    :', list1)
print('L2    :', list2)
list2.reverse()
list1.appendNode(list2.returnhead())
print('Merge :', list1)