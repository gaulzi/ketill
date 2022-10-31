
from card import Card
import random
NUMBER_CARDS = 13
WHOLE_DECK = 52
class Deck():
    def __init__(self):
        self.cards = []
        for suit in ["S", "H", "D", "C"]:
            for rank in range(1,14):
                self.cards.append(Card(rank,suit))

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            rand = random.randint(0,i)
            self.cards[i],self.cards[rand] = self.cards[rand],self.cards[i]

    def deal(self):
        self.card = self.cards[0]
        self.cards.remove(self.card)
        print("THISIS:{}".format(self.card))
        #return self.card

    def __str__(self) -> str:
        cards = ""
        count = 0
        for card in self.cards:
            count += 1
            cards += ("{:>3} ".format(str(card)))
            if count % NUMBER_CARDS==0:
                if count != WHOLE_DECK:
                    cards += "\n"
            
        return cards
            

