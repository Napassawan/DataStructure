def odd_even(arr, s):
    Ans = []
    if s == "Odd" :
        for i in range(0,len(arr)) :
            if i%2 == 0 :
                Ans.append(arr[i])

    if s == "Even" :
        for i in range(0,len(arr)) :
            if i%2 == 1 :
                Ans.append(arr[i])
    return Ans


print("*** Odd Even ***")
ls,arr,s = input("Enter Input : ").split(",")
Listarr = []
if ls == 'S' :
    for i in range(0, len(arr)):
        Listarr.append(arr[i])

if ls == 'L' :
    Listarr = arr.split(" ")

Ans = odd_even(Listarr, s)
if ls == 'S':
    for i in range(0, len(Ans)):
        print(Ans[i], end= "")
if ls == 'L':
    print(Ans)