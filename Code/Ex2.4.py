def sum5(list) :
    if(len(list) < 3):
        print("Array Input Length Must More Than 2")    
    else:
        num1 = []
        num2 = []
        for i in range(len(list)):
         for j in range(len(list)):
            for k in range(len(list)):
                if i < j < k:
                    if list[i] + list[j] + list[k] == 5:
                        num1.append(list[i])
                        num1.append(list[j])
                        num1.append(list[k])
                        num1.sort()
                        if num1 not in num2:
                            num2.append(num1)
                            num1 = []
                            continue
                        num1 = []
    print(num2)

list = list(map(int,input('Enter Your List : ').split()))
sum5(list)
