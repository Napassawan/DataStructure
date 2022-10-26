class Stack:

    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
        self.size = len(self.items)

    def push(self,i):
        self.items.append(i)
        self.size += 1

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        s = 'Value in Stack = '
        for ele in self.items:
            s+=str(ele)+' '
        return s  


AP = [i for i in(input('Enter Input : ').split(','))]
listAP = Stack()


for i in AP:
        if i[0] == "A" :
            listAP.push(i[2:])
            l = listAP.size
            print("Add = {} and Size = {}".format(i[2:],l))

        elif i == "P" :
            if listAP.isEmpty() == False:
                O = listAP.peek()
                P = listAP.pop()
                listAP.size -= 1
                l = listAP.size
                print("Pop = {} and Index = {}".format(O,l))
            else :
                print("-1")


if listAP.isEmpty() == True:
    print("Value in Stack = Empty")
else:
    print(listAP)


