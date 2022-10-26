class Queue:    
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
        self.size = len(self.items)

    def __str__(self):
        return "{}".format(self.items)

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


q = Queue()
nor, mirr = [e for e in input("Enter Input (Normal, Mirror) : ").split(' ')] 
mirr = list(mirr)
nor = list(nor)
mirr.reverse()

item = []
countMirr = 0
countNor = 0
fail = 0 
i = 0
x = 0
while i<len(mirr)-2:
  if(mirr[i]==mirr[i+1]==mirr[i+2]):
    q.enQueue(mirr[i])
    item.append(mirr[i])
    mirr.pop(i)
    mirr.pop(i)
    mirr.pop(i)
    countMirr += 1
    i=-1
  i+=1

while x < len(nor)-2:
  if(nor[x]==nor[x+1]==nor[x+2]):
    if(len(item)>0 ):
      nor.insert(x+2,q.deQueue())
      if(nor[x]==nor[x+1]==nor[x+2]):
        nor.pop(x)
        nor.pop(x)
        nor.pop(x)
        fail+=1
      del item[0]
    else:
      nor.pop(x)
      nor.pop(x)
      nor.pop(x)
      countNor+=1
    x=-1
  x+=1

print("NORMAL :")
print(len(nor))
if(len(nor)>0):
  nor.reverse()
  for i in nor:
    print(i,end = '')
  print()
else:
  print("Empty")

print("{} Explosive(s) ! ! ! (NORMAL)".format(countNor))

if(fail>0):
  print("Failed Interrupted {} Bomb(s)".format(fail))

print("------------MIRROR------------")
print(": RORRIM")
print(len(mirr))
if(len(mirr)>0):
  mirr.reverse()
  for j in mirr:
    print(j,end = '')
  print()
else:
  print("ytpmE")

print("(RORRIM) ! ! ! (s)evisolpxE {}".format(countMirr))