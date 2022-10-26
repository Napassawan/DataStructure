#drawpicfun
def draw(n,end):
    if end>0:
        print('_'*(end-1)+'#'*(n))
        draw(n+1,end-1)
    elif end<0:
        print('_'*n+'#'*(end*-1))
        draw(n+1,end+1)

ip = input("Enter Input : ")
ip = int(ip)
if ip > 0:
    draw(1,ip)
elif ip < 0:
    draw(0,ip)
else:
    print("Not Draw!")