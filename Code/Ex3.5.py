class Stack :
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == [] or len(self.items) == 0

    def size(self):
        return len(self.items)

def dec2bin(decnum):
    s = Stack()
    while decnum > 0:
            rem = decnum % 2
            s.push(rem)
            decnum //= 2
    bin = "" 
    while not s.isEmpty():
            bin = bin + str(s.pop())
    return bin



print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))