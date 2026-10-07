a = int(input("shu ru yi ge zheng zs"))
while a > 0:
	if a % 2 == 0:
		print(a)
		a = a // 2
	else:
		print(a)
		a = a * 3 + 1
	if a == 1:
		print(a)
		break
