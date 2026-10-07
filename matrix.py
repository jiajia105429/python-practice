import random
kong = []
for i in range(88):
	kong.append([])
	for j in range(88):
		kong[i].append(random.randint(0,1024))
target = int(input('zhengshu'))

for i in range(88):
	for j in range(88):
		if kong[i][j] == target:
			print(i,j) 
