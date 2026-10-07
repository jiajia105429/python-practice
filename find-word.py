text=input("shuru")
words=input("shuru")

words=words.split()

result=[]
for each in words:
	temp=text.find(each)
	while temp != -1:
		result.append([temp,temp+len(each)-1])
		temp=text.find(each,temp+1)
print(sorted(result))
