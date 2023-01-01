import random
class Card():

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.value = 0
        if self.rank == "A":
            self.value = 14
        elif self.rank == "J":
            self.value = 11
        elif self.rank == "K":
            self.value = 13
        elif self.rank == "Q":
            self.value = 12
        else:
            self.value = int(self.rank)


    def __repr__(self): #print()
        return self.rank + self.suit

    def __str__(self): #str()
        return self.rank + self.suit


class Deck():

    def __init__(self):
        self.SUITS = ["S", "C", "H", "D"] # list("SCHD")
        self.RANKS = [str(i) for i in range(2,11)] + ["A","J","K","Q"]
        self.build()
        self.shuffle()
        
    def build(self):
        self.deck = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card1 = Card(rank, suit)
                self.deck.append(card1)
    
    def __repr__(self):
        result = ""
        for card in self.deck:
            result += str(card) + " "
        return result

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        cardDealt = self.deck.pop(0)
        return cardDealt
    
    def deal_cards(self, numOfCards):
        cardsDealt = []
        for i in range(numOfCards):
            cardsDealt.append(self.deck.pop(0))
        return cardsDealt

if __name__ == "__main__":  #if running this file  __name__ = "__main__"         if running from module __name__ = "__module__"
    deck1 = Deck()
    print(deck1.deal_cards(5))
    print(deck1)
    c1 = Card("J","H")
    print(c1.value)



# colours = ["white", "black", "blue"]
# sizes = ["small", "medium", "large"]

# shirts = []
# for colour in colours:
#     for size in sizes:
#         shirts.append((colour, size))

# print(shirts)

# shirts = [(colour,size) for colour in colours for size in sizes]

