def factorial(num):
	fact = 1
	for i in range(1,num+1):
		fact = fact * i
	return fact

a = factorial(100)
b = 0
sum1 = 0
if a:
	b = list(str(a))
	for i in b:
		sum1 +=int(i)
print(sum1)

