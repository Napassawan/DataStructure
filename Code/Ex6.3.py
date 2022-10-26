#GCD
def GCD(x,y):
    x = abs(x)
    y = abs(y)
    if y==0:
        return x
    if x%y==0:
        return y
    else:
        return GCD(y,x%y)

x,y = map(int,input("Enter Input : ").split())
if y<0 and x==0:
    x,y =x,y
elif abs(y)>abs(x):
    x,y = y,x
if x==0 and y==0:
    print("Error! must be not all zero.")
else:
    print(f"The gcd of {x} and {y} is : {str(GCD(x,y))}")