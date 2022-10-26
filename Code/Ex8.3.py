

inp_ = input('Enter Input : ').split('/')
n = int(inp_[0])
l = [0]*(n+1)
node = [int(i) for i in inp_[1].split()]
len_ = len(node)
if (n - len_)*2+1 == n:
    for i in range(len_):
        l[len_+i] = node[i]
    for i in range(n-len_,0,-1):
        d = min(l[i*2],l[i*2+1])
        l[i] = d
        l[i*2] -= d
        l[i*2+1] -=d
    print(sum(l))
else:
    print('Incorrect Input')