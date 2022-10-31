
SUIT = "H","D","S","C"
RANK = 1,2,3,4,5,6,7,8,9,10,11,12,13,"A","J","Q","K"
class Card():
    def __init__(self,rank = 0, suit =""):
        self.rank = rank
        self.suit = suit
        if self.rank not in RANK or self.suit not in SUIT:
            self.rank = 0 
            self.suit = ""
        
    def is_blank(self):
        if self.rank == 0:
            return True
        return False

    def __str__(self) -> str:
        if self.suit == "":
            return("blk")
        if self.rank ==1:
            self.rank = "A"
        if self.rank == 11:
            self.rank = "J"
        if self.rank == 12:
            self.rank = "Q"
        if self.rank == 13:
            self.rank = "K"
        return("{:>2}{:>1}".format(self.rank,self.suit))

