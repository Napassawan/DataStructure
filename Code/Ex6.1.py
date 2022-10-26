#Fibonacci
def fibonacci(n):
	if n<=1:
		return n
	else:
		return(fibonacci(n-1) + fibonacci(n-2))

ip = int(input('Enter Number : '))
fi = fibonacci(ip)
print("fibo({}) = {}".format(ip,fi))
