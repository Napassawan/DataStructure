#Perket
S = list()
B = list()
Sol = list()

def perket(ip, num, b, s):
    if(ip == len(n)):
        if(num != 0):
            Sol.append(abs(b-s))
        return;
    ss = s * int(S[ip])
    bb = b + int(B[ip]) 
    perket(ip + 1, num, b, s)
    perket(ip + 1, num + 1, bb, ss)
    
    
n = input('Enter Input : ').split(',')
for i in n:
    s, b = i.split()
    S.append(s) 
    B.append(b)
S.append(0) 
B.append(0) 
perket(0, 0, 0, 1)
print(min(Sol))