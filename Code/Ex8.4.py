def Mondstadt(n):
    sum = 0                            
    if n >= len(pow):             
        return 0
    sum += Mondstadt(2*n + 1)     
    sum += Mondstadt(2*n + 2)     
    return pow[n] + sum           

pow, group = input('Enter Input : ').split('/')
pow = [int(i) for i in pow.split()]
group = [str(i) for i in group.split(',')]
print(Mondstadt(0))                 
for x in range(len(group)):
    i,j = group[x].split()
    G1 = Mondstadt(int(i))        
    G2 = Mondstadt(int(j))          
    if G1 > G2 : print("{}>{}".format(i,j))
    elif G1 < G2 : print("{}<{}".format(i,j))
    else : print("{}={}".format(i,j))