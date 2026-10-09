users={"jiajia":123456,"jiayu":112233}
print("Registration")

while True:
	name=input("name")
	if name in users:
		print("already exists! try another")
		contiune
	password=input("password")
	users[name]=password
	print("success!")
	if input("continue?(Y/N)" )!= 'Y':
		break
print("datebase",users)
