first_number = -1
second_number = 1
c= 0
sum1 = 0 
while first_number< 4000000:
	c = first_number + second_number
	first_number = second_number
	second_number = c

	if c % 2 ==0:
		sum1+=c
print(sum1)