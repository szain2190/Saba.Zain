from Deck import Deck
from Player import Player,HumanPlayer, AIPlayer
class Blackjack():

    def __init__(self):
        self.game()




    
    def game(self):
        deck1 = Deck()
        player1 = HumanPlayer("Saba")
        dealt = deck1.deal_cards(2)
        player1.takeCards(dealt)
        player1.turn(deck1)
        player2 = AIPlayer("computer")
        dealt = deck1.deal_cards(2)
        player2.takeCards(dealt)
        player2.turn(deck1)
        if player1.busted == True:
            print(player1.name, "lost")
        elif player2.busted == True:
            print(player2.name, "lost")
        elif player2.score >= player1.score:
            print(player1.name, "has", player1.score)
            print(player2.name, "has", player2.score)
            print(player2.name, "won")
        elif player1.score >= player2.score:
            print(player1.name, "has", player1.score)
            print(player2.name, "has", player2.score)
            print(player1.name, "won")

if __name__ == "__main__":
    bj = Blackjack()
