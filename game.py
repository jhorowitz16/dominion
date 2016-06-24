from card import Card
from deck import Deck

# Simulate an actual game (for a single person)

DEBUG = True 

class Game:

        def __init__(self):
                # initialize the starting deck here instead
                self.deck = Deck()
                self.turn = 0
                self.deck.fullPrint(self.turn)

        # note the constructor already initialized the deck, plus it is already shuffled 
        def setup(self):
                pass
        

        # ABC
        # Action
        # Buy
        # Collect
        def takeTurn(self):
                return_info = {} # for playing around with events - to get feedback in main

                self.turn += 1
                self.deck.drawHand()
                self.deck.fullPrint(self.turn) # hand right after drawing it
                return_info['money'] = self.deck.calcHandMoney()
                return_info['turn'] = self.turn
                return_info['vp'] = self.deck.total_vp
                self.moneyBuy(True) 

                self.deck.cleanUp()

                return return_info 


        # choose what to buy...
        # if provinces is set to true, buy provinces in addition to silvers and golds
        def moneyBuy(self, provinces=False):
                money = self.deck.calcHandMoney()
                dp("money: " + str(money))
                if money >= 8 and provinces:
                        dp("province")
                        self.deck.addCardType('PROVINCE')
                elif money < 3:
                        return
                elif money < 6:
                        dp("silver")
                        self.deck.addCardType('SILVER')
                else:
                        dp("gold")
                        self.deck.addCardType('GOLD')


# debug print - same as print iff debug is true
def dp(print_str):
        if DEBUG:
                print(print_str)
