def getchar(str_):
    str_ = str(str_)
    for i in range(0,len(str_)):
        if str_[i].isalpha():
            return str_[i]

def Bubble(li):
    for i in range(0,len(li)-1):
        for j in range(0,len(li)-i-1):
            if getchar(li[j]) > getchar(li[j + 1]):
                li[j], li[j + 1] = li[j + 1], li[j]
    return ' '.join(li)

inp = input('Enter Input : ').split()
print(Bubble(inp))