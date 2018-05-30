import random
number=random.randint(1,9)
guess=0
count=0

while guess!=number and guess!="exit":
	guess=input("guess: ")
	if guess == "exit":
		break
	guess=int(guess)
	count=count+1
	if guess>number:
		print("Za duzo")
	elif guess==number:
		print("Brawo")
		print(count)
		break
	elif guess<number:
		print("Za malo")