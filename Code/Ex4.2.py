class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        self.items.pop(0)
    def isEmpty(self):
        return self.items == []
        #return len(self.items) == 0
    def size(self):
        return len(self.items)
    def __str__(self):
        s = ""
        for ele in self.items:
            if(ele==self.items[len(self.items)-1]):
                s += str(ele)
            else:
                s+=str(ele)+", "
        return s


inp = input("Enter people : ")

q = Queue()
q1 = Queue()
q2 = Queue() 

n=0
e2=0
e3=0

if(inp!=[] ):
    if(inp!=''):
        for e in inp:
            q.enQueue(e)
    else:
        n=1
else:
    n=1

if(n!=1):
    for e1 in range(len(q.items)):
        
        if(e1 != 0 and e1 % 3 == 0 ):
            q1.deQueue()
        else:
            pass

        if(q1.size()<5):
            if(q.size()!=0):
                q1.enQueue(q.items[0])
                q.deQueue()
            else:
                pass  
        elif(q1.size()==5 and q2.size()<5):
            if(q.size()!=0):
                q2.enQueue(q.items[0])
                q.deQueue()
            else:
                pass        
        else:
            pass

        if(q2.size()>=1):
            if(e3!=0 and e3%2==0):
                q2.deQueue()
            else:
                pass
            e3+=1    
        else:
            pass
        
        print(e1+1,q.items,q1.items,q2.items)
        