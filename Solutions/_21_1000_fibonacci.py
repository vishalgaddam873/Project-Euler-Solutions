
f_number = -1
s_number = 1
t_number = 0
new_list = []
while True:
	t_number = f_number + s_number
	f_number = s_number
	s_number = t_number
	if len(str(t_number)) == 1000:
		new_list.append(str(t_number))
		break
	else:
		new_list.append(str(t_number))

b = len(new_list)
c = b - 1
print(c)
