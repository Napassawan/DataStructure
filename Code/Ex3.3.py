class Stack:

    def __init__(self):
        self.s = []

    def push(self, value):
        self.s.append(value)

    def pop(self):
        self.s.pop()

    def size(self):
        return len(self.s)

    def isEmpty(self):
        if len(self.s) == 0:
            return True
        else:
            return False

    def returnL(self):
        return self.s[-1]

    def __str__(self):
        return (f'{self.s}')

    def find(self, value):
        if value in self.s:
            return True
        else: return False

inp = [i for i in input('Enter Infix : ')]

S = Stack()
postfix = []
Operator = ['+','-','*','/','^','(',')']

for i in inp:
    if i not in Operator:
        postfix.append(i)
    else:
        if i == ')':
            while S.returnL() != '(':
                postfix.append(S.returnL())
                S.pop()
            S.pop()
        elif i == '^':
            if not S.isEmpty():
                if S.returnL() == '^':
                    postfix.append((S.returnL()))
                    S.pop()
                    S.push(i)
                else: S.push(i)
            else: S.push(i)
        elif i == '/' or i == '*':
            if not  S.isEmpty():
                if S.returnL() == '^' or S.returnL() == '/' or S.returnL() == '*':
                    postfix.append((S.returnL()))
                    S.pop()
                    S.push(i)
                else: S.push(i)
            else: S.push(i)
        elif i == '+' or i == '-':
            if not S.find('('):
                while not S.isEmpty()  :
                    postfix.append(S.returnL())
                    S.pop()
                S.push(i)
            else:
                while not S.returnL() == '('  :
                    postfix.append(S.returnL())
                    S.pop()
                S.push(i)

        else : S.push(i)

while not S.isEmpty():
    postfix.append(S.returnL())
    S.pop()

print('Postfix : ',end='')
print(*postfix,sep='')