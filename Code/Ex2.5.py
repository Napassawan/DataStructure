def bon(w):
	l = []
	for letter in w:
  		number = ord(letter) - 96
  		l.append(number)

	for i in range(len(l)):
    	 for j in range(len(l)):
			    if i < j:
					   if l[i] == l[j]:
						     ans = int(l[i])
	ans *= 4
	return ans

secretCode = input("Enter secret code : ")
print(bon(secretCode))