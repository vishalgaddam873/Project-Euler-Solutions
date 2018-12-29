sum1 = 0
sum_of_square = 0
square_of_sum = 0
difference = 0
for i in range(1,101):
	sum_of_square = i ** 2
	sum1 +=sum_of_square
	square_of_sum += i 
square = square_of_sum ** 2
difference = square - sum1
print(difference)