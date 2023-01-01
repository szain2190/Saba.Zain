from Deck import Card
class Evaluater:


    def sort_key(self,card):
        return card.value

    def bestHand(self, hand, table):

        cards = sorted(hand+table, key=self.sort_key, reverse=True)

        if self.royal_flush():
            pass
        elif res:= self.four_of_a_kind(cards):
            print("you have four of a kind of", res)
        elif res:= self.flush(cards):
            print("you have a flush of", res[0], "and", res[1])
        elif res:= self.straight(cards):
            print("you have a straight with", res)
        elif res:= self.three_of_a_kind(cards):
            print("you have three of a kind of", res)
        elif res:= self.two_pair(cards):  # 9 9 4 4   res = [9,4]
            print("you have two pair", res[0], "and", res[1])
        elif res:= self.pair(cards): # res = "3" True      res = None False
            print("you have a pair of", res)
        else:
            print("high card is", self.high_card(cards))



    def royal_flush(self):
        pass

    def four_of_a_kind(self, cards):
        counter = 0  # A K K K 4
        current_rank = "" #"K"
        for card in cards:
            if card.rank == current_rank: # K   K
                counter += 1
                if counter == 4:
                    return current_rank
            else:
                counter = 1
                current_rank = card.rank


    def flush(self,cards):
        suit_list = []
        for card in cards:
            suit_list.append(card.suit) # ["S", "H", "H", "H", "H" "H"]


        for suit in "HSCD":
            count = suit_list.count(suit)
            if count >= 5:  #suit = "H"
                for card in cards:
                    if card.rank == suit:
                        return [suit, card.rank]



        #my_list = [3,6,4,8,9,7,3,7,3]
        #count_3 = my_list.count("3")



    def straight(self,cards):   # K 9 8 8 7 6 5 3    A -- K       14 -- 13
        previous_card = cards[0]
        counter = 1
        highest_card = cards[0]
        for card in cards:
            if card.value == previous_card.value - 1:  # two card are consecutive
                counter += 1
            elif card.value == previous_card.value: # two cards are equal rank
                pass
            else:
                counter = 1 #starting a new run
                highest_card = card
            previous_card = card
            if counter == 5:
                return highest_card.rank



    def three_of_a_kind(self,cards): # loop through hand, if three card have same rank return rank of card
        counter = 0  # A K K K 4
        current_rank = "" #"K"
        for card in cards:
            if card.rank == current_rank: # K   K
                counter += 1
                if counter == 3:
                    return current_rank
            else:
                counter = 1
                current_rank = card.rank

    def two_pair(self, cards): # how to detect 2 pairs and return there rank    A K J 5 5 4  cards = [Card("A", "H"),]
        firstPair = self.pair(cards) # "5" --> True     None --> False

        # make a new list of just the ranks   rank_list = ["A", "K", "K"]
        rank_list = []
        for card in cards:
            rank_list.append(card.rank)
        index = rank_list.index(firstPair) #1

        secondPair = self.pair(cards[index+2:]) #None

        if firstPair and secondPair:
            return [firstPair, secondPair]  # "5" == True









    def pair(self,cards):  # loop through hand, if two consecutive cards have same rank return rank of card
        previous_card = ""   #  A K K 4
        for card in cards:
            if card.rank == previous_card:  # "A" == ""
                return card.rank
            previous_card = card.rank

        


    def high_card(self, cards):
        return cards[0].rank
        # currentCard = 0
        # rank = 0
        # for card in cards:
        #     if card.value > currentCard:   #Card() > 0
        #         currentCard = card.value
        #         rank = card
        # return rank

if __name__ == "__main__":
    hand = [Card("5", "D"), Card("4", "H")] #5     5
    table = [Card("3", "H"), Card("8", "H"), Card("9", "H"), Card("7", "H"), Card("2", "H")]
    eval = Evaluater()
    eval.bestHand(hand, table)






