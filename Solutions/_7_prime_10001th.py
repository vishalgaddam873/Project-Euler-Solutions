def prime_number(num):
	flag = 0
	counter = 2
	while counter<=(num**0.5):
		if num % counter==0:
			break
		counter +=1
	else:
		return True
	
def any_prime(number):	
	counter1 = 0
	value = 2
	while True:
		if prime_number(value):
			counter1 +=1
			print(value)
		if counter1 == number:
			print(value)
			break
		value +=1	
any_prime(100)

