class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.busted = False
        self.score = 0

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

    def calcScore(self):  # A 9 A     31  2A     31 -10 = 21   
        self.score = 0
        ace = 0
        for card in self.hand:
            if card.rank == "A":
                self.score += 11
                ace += 1
            elif card.rank in ["J","Q","K"]:
                self.score += 10
            else:
                self.score += int(card.rank)

        while self.score >= 21 and ace > 0:
            self.score -= 10
            ace -= 1

class HumanPlayer(Player):

    def __init__(self, name):
        super().__init__(name)

    def turn(self, deck):
        stick = False
        print(self)
        self.calcScore()
        print(self.score)
        while stick is not True and self.busted is not True:
            option = input("Would you like to (h)it or (s)tick: ").lower()
            if option == "s":
                print("They chose to stick")
                stick = True
            elif option == "h":
                dealtCard = deck.deal_card()
                self.takeCard(dealtCard)
                print(self)
                self.calcScore()
                print(self.score)
                if self.score > 21:
                    print(f"{self.name} has busted")
                    self.busted = True




class AIPlayer(Player):

    def __init__(self, name):
        super().__init__(name)

    def turn(self, deck):
        print(self)
        self.calcScore()
        print(self.score)
        while self.score < 15:
            print(self.name, "choose to hit")
            dealtCard = deck.deal_card()
            self.takeCard(dealtCard)
            print(self)
            self.calcScore()
            print(self.score)
            if self.score > 21:
                print(f"{self.name} has busted")
                self.busted = True
        if not self.busted:
            print(self.name, "choose to stick")


