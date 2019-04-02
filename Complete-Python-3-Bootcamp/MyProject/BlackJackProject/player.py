from carddeck import Card

class Hand:
	def __init__ (self):
		self.cards = []
		self.value = 0
		self.aces = 0
	def adjust_for_ace(self):
		while self.value > 21 and self.aces > 0:
			self.value -= 10
			self.aces -= 1
	def add_card (self,card):
		self.cards.append(card)
		self.value += card.value
		if card.rank == "Ace":
			self.aces += 1
			self.adjust_for_ace()
	def __str__ (self):
		ans = "value: {}\n number of aces: {}\ndeck:\n".format(self.value, self.aces)
		for item in self.cards:
			ans += "{} of {}\n".format(item.rank, item.suit)
		return ans

if __name__ == "__main__":
	playerhand = Hand()
	samplecard1 = Card("Hearts", "Ace")
	samplecard2 = Card("Clubs", "Ace")
	samplecard3 = Card("Clubs", "Ace")
	samplecard4 = Card("Hearts", "Five")

	playerhand.add_card(samplecard1)
	playerhand.add_card(samplecard2)
	playerhand.add_card(samplecard3)
	playerhand.add_card(samplecard4)
	print(playerhand)

