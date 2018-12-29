def palindrome(string):
	string = str(string)
	pali = string[::-1]
	if pali == string:
		return True
	else:
		return False
a = 0
for i in range(100,1000):
	for j in range(100,1000):
		product = i * j
		if palindrome(product):
			if product > a:
				a= product
print(a)