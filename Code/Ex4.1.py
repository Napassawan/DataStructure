class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
        self.size = len(self.items)

    def isEmpty(self):
        return self.items == []

    def enqueue(self, items):
        self.items.append(items)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)        

x = [i for i in(input('Enter Input : ').split(','))]
q = Queue()

for i in x:
    if i[0] == 'E':
        q.enqueue(i[2:])
        l = q.size
        print("Add {} index is {}".format(i[2:],l))
        q.size += 1
    elif i[0] == 'D':
        if q.isEmpty() == False:
            q.size -= 1
            l = q.size
            print("Pop {} size in queue is {}".format((q.items[0]),l))
            q.dequeue()
        else:
            print("-1")
if q.isEmpty() == True:
    print("Empty")
else:
    print("Number in Queue is :  {}".format(q.items))