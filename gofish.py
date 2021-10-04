import random

cards = []
player1 = []
player2 = []

def first_shuffle():
	for i in range(4):
		for card in range(1,14,1):
			cards.append(card)
	
	for i in range(7):
		x = cards.pop(random.randrange(len(cards)))
		player1.append(x)
		y = cards.pop(random.randrange(len(cards)))
		player2.append(y)

#def game_seq(Player, Choice):
	

#def scooring(p)
#	score[p] +=1


def check_4_a_match(player):
	if player ==1:
		for i in range(len(player1)):
			match = 0
			for j in range(i+1,len(player1)):
				if player1[i]==player1[j]:
					match +=1
#				if match == 3:
#					score(1)
			print(f"the number {player1[i]} has {match} matches")
	elif player == 2:
		 for i in range(len(player1)):
                        match = 0
                        for j in range(i+1,len(player1)):
                                if player1[i]==player1[j]:
                                        match +=1
#                               if match == 3:
#                                       score(1)
                        print(f"the number {player1[i]} has {match} matches")

def look_for_cards1(i):
	for j in player2:
		if j==i:
			player1.append(player2.pop(j))
		
#def first_player_turn():
	

first_shuffle()



print (cards)
print(len(cards))
print(player1)
print(player2)	
look_for_cards1(int(input("whitch card you would like to ask your aponant for?")))
print(player1)
print(player2) 
#check_4_a_match(int(input("whitch player?> ")))

