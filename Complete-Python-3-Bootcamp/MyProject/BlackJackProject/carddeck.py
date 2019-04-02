from random import shuffle

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 
			'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
	def __init__ (self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]
	def __str__ (self):
		return "{} of {}".format(self.rank, self.suit)

class Deck:
	def __init__ (self):
		self.deck = []
		self.suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
		self.ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 
			'Jack', 'Queen', 'King', 'Ace')
		for suit in self.suits:
			for rank in self.ranks:
				self.deck.append(Card(suit,rank))
	def suffer (self):
		shuffle(self.deck)
	def deal (self):
		card = self.deck.pop()
		return card
	def __str__ (self):
		ans = ""
		for item in self.deck:
			ans += str(item)+"\n"
		return ans

if __name__ == "__main__":
	test_desk = Deck()
	print(test_desk)
	test_desk.suffer()
	print(test_desk)
	print(len(test_desk.deck))
	print(test_desk.deal())
	samplecard = Card("Hearts", "Two")
	print(samplecard)