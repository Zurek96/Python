import sys
number=int(input("Number: "))

def prime(number):
	for i in range(2,number-1):
		if number%i!=0:
			continue
		elif number%i==0:
			sys.exit("Nie pierwsza")	
	return("pierwsza")
	

print(prime(number))