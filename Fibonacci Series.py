#This is the code for the Fibonacci Series
n = int(input("Enter the number of your choice :"))
a = -1
b = 1
c = 0
while c <= n:
	c = a + b
	print(c)
	a = b
	b = c