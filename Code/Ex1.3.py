print("*** Election ***")
p = int(input("Enter a number of voter(s) : "))
vote = input('').split()
list = []

for x in vote:
    if(int(x)>0 and int(x)<=20):
        list.append(x)

if len(list) <= 0:
    print("*** No Candidate Wins ***")
else :
    print(max(set(list), key=list.count))


