from Deck import Deck
from Poker_player import Poker_player, AIPlayer

class Poker:
    
    def __init__(self):
        pass


    def game(self):
        quit = False
        while quit is not True:
            deck1 = Deck()
            player1 = Poker_player("Saba")
            player2 = AIPlayer("Computer")
            dealt = deck1.deal_cards(2)
            player1.takeCards(dealt)
            dealt = deck1.deal_cards(2)
            player2.takeCards(dealt)
            table = Poker_player("T")
            dealt = deck1.deal_cards(5)
            table.takeCards(dealt)
            print(player1)
            print(player2)
            print(table)
            option = input("Would you like to (q)uit or (c)ontinue? ")
            if option == "q":
                quit = True

if __name__ == "__main__":
    poker = Poker()
    poker.game()
    