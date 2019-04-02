class Chips:
	def __init__ (self):
		self.total = 100
		self.bet = 0
	def buy_more (self):
		ans = input("Do you want to buy more chips?(Y/N)  ")
		if ans == "Y":
			try:
				value = int(input("How much?  "))
			except:
				print("Invalid input, try again")
				self.buy_more()
			else:
				self.total += value
		elif ans != "N":
			print("Invalid input, try again")
			self.buy_more()
	def take_bet (self):
		print ("\n"*25)
		print (self)	
		while True:
			try:
				bet = int(input("Take your bet!  "))
			except:
				print ("Invalid input, try again")
				continue
			if bet > self.total:
				print("Your bet shouldn't except {}$".format(self.total))
				self.buy_more()
			elif bet <= 0:
				print("Your bet should more than 0$")
			else:
				self.bet = bet
				break
			
	def win_bet (self):
		self.total += self.bet
	def lose_bet (self):
		self.total -= self.bet
	def __str__ (self):
		return "Money remain: {}$".format(self.total)

if __name__ == "__main__":
	player = Chips()
	player.take_bet(200)
	player.win_bet()
	print(player)
