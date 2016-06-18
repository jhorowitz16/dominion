from random import *

# Deck.py

# deck class for dominion


class Deck:

	deck_id = 0
	player = "player1"
	name = "the deck"
	total_vp = 0
        total_worth = 0
	av_worth = 0

        # represent the cards in a deck as a list of Card objects

        # this is the full deck - two smaller lists representing the discard and the other list

	cards = []
        pile = [] # this is the "deck" in the traditional sense of the cards yet to play...
        discard = []
        hand = []

	money_types = ['copper', 'silver', 'gold']
	victory_types = ['estate', 'duchy', 'province']
	action_types = ['village', 'smithy']
	all_types = money_types + victory_types + action_types

	def __init__(self, deck_id=0, player="player", name="deck", cards=[]):
		self.deck_id = deck_id 
		self.player = player
		self.name = name
		self.total_vp = self.calcTotalVPs()
		self.total_worth = self.calcTotalWorth()
                self.av_worth = self.total_worth / len(cards)
                self.cards = cards


        ###### add and remove cards ######

	# two versions of add card - one that takes a type (string) and one that takes an actual card object
	def addCard(self, card):
		if card:
			cards += card
			count += 1
			av_worth += (av_worth*count + card.worth) / count
			total_vp += card.vp
		else:
			return false

	def addCardType(self, type_str):
		if type_str in all_types:
			# make a card and add it
			new_card = Card(type_str)
			addCard(self, new_card)

		else:
			return false

	# remove a card based on its unique id
	def removeCard(self, id):
                pass



        ###### helper methods for simple calculations ###### 

        # calculate the total 'worth' of the deck based on the initial list of cards passed into the constructor 
        def calcTotalWorth(self):
                total = 0
                for card in self.cards:
                        total += card.worth
                return total

        # count all the victory points in the initial list of cards
        def calcTotalVPs(self):
                total = 0
                for card in self.cards:
                        total += card.worth
                return total
       
        # not sure if this will be useful...
        def calcTotalMoney(self):
                total = 0
                for card in self.cards:
                        total += card.money
                return total



        ###### shuffling ######

        # do NOT shuffle the deck - instead shuffle the pile - let the deck be a clean copy of all cards owned

        def reshuffle(self):
                shuffle(self.discard)
                self.cards += self.discard
                self.discard = []



        ###### game actions ######

        # draw hand default is 5 cards, without expansions....
        def drawHand(self):
                left_to_deal = 5
                while left_to_deal > 0:
                        if len(self.pile) > 0:
                                self.hand.append(self.pile.pop())
                                left_to_deal -= 1 
                        else:
                                # need to reshuffle
                                self.reshuffle()

        # end of turn, discard hand (and all played cards)
        def handToDiscard(self):
                discard += hand
                hand = []



        ###### string related utils ######

        def __repr__(self):
                return self.name + '_' + str(self.deck_id)

        def __str__(self):
                return str(self.cards)

        def fullPrint(self):
                print("Hand: " + self.hand)
                print("Discard: " + self.discard)
                print("All Cards: " + self.cards)
