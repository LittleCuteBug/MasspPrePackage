def display(player,dealer,chips,flag):
	# flag == true -> display all cards
	# flag == false -> display some cards
	print("\n"*25)
	print(chips)
	print("Your bet: {}$".format(chips.bet))
	print("\n"+"-"*25+"\n")
	print("Dealer cards: ")
	if flag:
		for card in dealer.cards:
			print(card)
		print("Dealer point: {}".format(dealer.value))
	else:
		print(dealer.cards[0])
		print("unknown card")
	print(" ")
	print("Your cards: ")
	for card in player.cards:
		print(card)
	print("\nYour point: {}".format(player.value))
	print("\n"+"="*25)