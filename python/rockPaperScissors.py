player1=input("Player1: ")
player2=input("Player2: ")
def compare(u1, u2):
	if u1==u2:
		return("It's a tie")
	elif u1=='r':
		if u2=='s':
			return("P1 wins")
		else:
			return("P2 wins")
	elif u1=='r':
		if u2=='p':
			return("P2 wins")
		else:
			return("P1 wins")
	elif u1=='p':
		if u2=='s':
			return("P2 wins")
		else:
			return("P1 wins")
	else:
		return("Cos nie tak")
	sys.exit()

print(compare(player1, player2))