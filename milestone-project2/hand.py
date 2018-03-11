from deck import Deck, values

class Hand():

	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0
	
	def add_card(self, card):
		self.cards.append(card)
		self.value += values[card.rank]

		# TRACK ACES
		if card.rank == 'Ace':
			self.aces += 1
	
	def adjust_for_ace(self):
		# IF TOTAL VALUE > 21 AND I STILL HAVE AN ACE
		# THAN CHANGE MY ACE TO BE A 1 INSTEAD OF AN 11

		while self.value > 21 and self.aces > 0:
			self.value -= 10
			self.aces  -= 1

test_player = Hand()
