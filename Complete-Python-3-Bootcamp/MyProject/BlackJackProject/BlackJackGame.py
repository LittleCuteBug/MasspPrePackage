from carddeck import Card
from carddeck import Deck
from player import Hand
from chips import Chips
from display import display

playing = None
playagain = True


def hit (hand, deck):
	hand.add_card(deck.deal())
def stand ():
	global playing 
	playing = False
def hit_or_stand(hand,deck):
	ans = input("Hit or Stand (Hit/Stand) ")
	if ans == "Hit":
		hit(hand,deck)
	elif ans == "Stand":
		stand()
	else:
		print("Invalid input")
		hit_or_stand(hand,deck)
def dealer_decision(hand,deck,playervalue):
	if hand.value < playervalue: 
		hit(hand, deck)
	elif hand.value == playervalue:
		if hand.value < 17:
			hit(hand, deck)
		else:
			stand()
	else:
		stand()

def bust(hand):
	return hand.value > 21
def player_win ():
	print("You win!!!")
	playerchip.win_bet()
def player_lose ():
	print("You lose!!!")
	playerchip.lose_bet()


playerchip = Chips()
	
while playagain:
	deck = Deck()
	deck.suffer()
	playerhand = Hand()
	dealerhand = Hand()
	playerchip.take_bet()

	hit(playerhand,deck)
	hit(playerhand,deck)

	hit(dealerhand,deck)
	hit(dealerhand,deck)

	display(playerhand,dealerhand,playerchip,False)

	#while playing:
	print("Your turn")
	playing = True
	while (not bust(playerhand) and playing):
		display(playerhand,dealerhand,playerchip,False)
		hit_or_stand(playerhand,deck)
	else:
		if bust(playerhand):
			display(playerhand,dealerhand,playerchip,True)
			print ("BUST!!!")
			player_lose()
		else:
			print("Dealer turn")
			playing = True
			while (not bust (dealerhand) and playing):
				display(playerhand,dealerhand,playerchip,True)
				input()
				dealer_decision(dealerhand,deck,playerhand.value)
			else:
				if bust(dealerhand):
					display(playerhand,dealerhand,playerchip,True)
					print ("Dealer BUST!!!")
					player_win()
				else:
					if dealerhand.value > playerhand.value:
						display(playerhand,dealerhand,playerchip,True)
						player_lose()
					elif dealerhand.value == playerhand.value:
						display(playerhand,dealerhand,playerchip,True)
						print("Tie!!! It's a push")
					elif dealerhand.value < playerhand.value:
						display(playerhand,dealerhand,playerchip,True)
						player_win()
	again = input ("Play again? (Y/N)")
	if again == "N":
		playagain = False










