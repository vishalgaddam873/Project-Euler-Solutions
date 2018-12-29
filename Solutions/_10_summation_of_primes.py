def prime(num):
	flag = 0
	counter = 2
	while counter <=(num**0.5):
		if num % counter== 0:
			break
		counter +=1
	else:
		return True
def sum_of_primes(num):
	sum1 = 0
	for i in range(2,num):
		if prime(i):
			sum1+=i
	return sum1
a = sum_of_primes(2000000)
print(a)
