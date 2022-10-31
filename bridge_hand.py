from card import Card
from deck import Deck,NUMBER_CARDS


class BridgeHand():
    NUMBER_CARDS = 13
    def __init__(self):
        self.hand = []
        for card in range(NUMBER_CARDS):
            card = Card()
            self.hand.append(card)

    def add_card(self,card): 
            if str(self.hand)=="blk":
                self.hand= card
                return self.hand
    
    def __str__(self) -> str:
        cards = ""
        for card in self.hand:
            cards += ("{:>2} ".format(str(card)))  
        return cards
            