import random

answer = random.randint(1,10)
counts=3

while counts>0:
	temp = input("guess a number (1-10): ")
	guess = int(temp)  #guess=int(input("guess a number (1-10)")

	if guess== answer:
		print("correct")
		break
	else:
		if guess < answer:
			print("too small")
		else:
			print("too big")
	counts = counts-1

print("game over") 
