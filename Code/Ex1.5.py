x = int(input("Enter Input : "))
r=4+(x*2)
d=r/2
num=0

for i in range(int(d)):
    for j in range(1,r+1):
        if(j<((r/2)-i)):
            print(".", end ="")
        elif(j>=((r/2)-i) and j<=(r/2)):
            print("#", end ="")
        elif(i==0):
            print("+", end ="")
        elif(i==d-1):
            print("+", end ="")
        elif(i<d and j==d+1):
            print("+", end ="")
        elif(i<r/2 and j<r):
             print("#", end ="")
        elif(i<r/2 and j==r):
             print("+", end ="")
    print("")

for i in range(int(d),r):
    for j in range(1,r+1):
        if(i==d and j<=d):
            print("#", end ="")
        elif(i==d and j<=r):
            print("+", end ="")
        elif(i==r-1 and j<d):
            print("#", end ="")
        elif(i<r and j==1):
            print("#", end ="")
        elif(i<r and j<d):
            print("+", end ="")
        elif(i<r and j==d):
            print("#", end ="")
        elif(i<r and j<=(r-num)):
            print("+", end ="")
        elif(i<r and j<=r):
            print(".", end ="")
    num+=1
    print("")