def prime_number(num):
	flag = 0
	counter = 2
	while counter<=(num**0.5):
		if num % counter==0:
			break
		counter +=1
	else:
		return True
	

# This  is code for largest prime factor

num = 600851475143
flag = 0
counter1 = 2
new_list =[]
while counter1<=(num**0.5):
	if num % counter1==0:
		new_list.append(counter1)
	counter1 +=1
b = []
for  i in new_list:
	if prime_number(i):
		b.append(i)
print(max(b))
