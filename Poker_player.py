class Poker_player:

    def __init__(self, name):
        self.name = name
        self.hand = []
    

    def takeCard(self, card):
        self.hand.append(card)

    def takeCards(self, cards):
        for card in cards:
            self.hand.append(card)

    def __repr__(self):
        result = ""
        result += self.name + " has "
        for card in self.hand:
            result += str(card) + " "
        return result

class AIPlayer(Poker_player):
    pass