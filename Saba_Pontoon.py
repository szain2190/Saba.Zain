import random # importing the random library
deck = [] # global variable so can be used anywhere in the code
playerhand = [] # can also be used anywhere in the code
cmpHand = [] # can also be used anywhere in the code

 
def buildDeck(): # to build the deck
    deck.clear() # to make sure the deck is empty
    playerhand.clear() # to make sure the playerhand is empty
    cmpHand.clear() # to make sure the computer hand is empty
    value = ["Ace","two","three","four","five","six","seven","eight","nine","ten", "Jack", "Queen", "King"] 
    # the values of the cards as strings

    for i in value: # nested loop to append every item in value to deck
         for j in range(4):
            deck.append(i)



def dealCard(): # to deal the cards out
    x = random.randint(0,len(deck) - 1) # picked out a random number
    card = deck[x] # taking a card out of the deck
    print("\ncard dealt " + (card)+"\n") # let player know what card they were dealt
    deck.pop(x) # removed the card from the deck
    return card # returned the value of the card

def score(hand): # to give the player their score of the cards
    count = 0 # to store the score
    for item in hand: # loop to add their score depending on their cards
        if item == "Ace": # big if statement to add the right amount of points depending on their cards
            count = count + 1
        elif item == "two":
            count = count + 2
        elif item == "three":
            count = count + 3
        elif item == "four":
            count = count + 4
        elif item == "five":
            count = count + 5
        elif item == "six":
            count = count + 6
        elif item == "seven":
            count = count + 7
        elif item == "eight":
            count = count + 8
        elif item == "nine":
            count = count + 9
        else:
            count = count + 10
    return count # returns their score to them

def currenthand(): # to display what they have in their hand after being dealt the cards
    print("\nYour hand is:") # to tell them that their current hand in being displayed
    for i in playerhand: # loop to print their cards in their hand
        print(str(i),end = " ") # prints a new line
    print("\n\nYour score is " +str(score(playerhand))) # prints their score in their hand
    if score(playerhand) > 21: # if statement to check their hand is greater than 21
        print("\nYou busted") # displays message if the if statement is true
        gameOver() # calls gameOver function so message can be displayed 


def option(): # to display message if they want another card or not
    answer = input("\nDo you want to twist or stick: \n") # outputs question on the screen for them to answer
    if answer == "stick": # if statement, if their answer is stick
        cmpTurn() # calls cmpTurn function
    elif answer == "twist": # if the choose to twist
        twist()# calls twist function
    else: 
        print("\nInvalid input, try again") # outputed on the screen if their is an error in their input
        option() # option function is then displayed again

def cmpTurn(): # lets the computer have a turn
    print("\n*****************************************") # new line spaces it out
    print("\nNow its the computers turn") # tells player it is the computer's turn
    cmpHand.append(dealCard()) # deals the computer a card
    cmpHand.append(dealCard()) # deals the computer a card again
    cmpScore = score(cmpHand) # adds the score of the computers hand to the variable cmpScore
    print("\nThe computers score is",cmpScore) # tells the player the computer's score
    while cmpScore < score(playerhand): # while loop to check that the computer's score is bigger than the players score
        print("\nThe computer has chosen to twist") # tells the player what the computer chose to do
        cmpHand.append(dealCard()) # deals the computer a card
        cmpScore = score(cmpHand) # adds the score of the computers hand to the variable cmpScore
        print("\nThe computers score is now",cmpScore) # tells the player the computer's score
        if cmpScore > 21:  #checks if the computer's score is bigger than 21
            print("\nThe computer busted.\n\nYou won!!!") # tells the player they won
            gameOver() # calls gameOver function
    print("\nThe computer won") # tells the player the computer won 
    gameOver() # calls gameOver function

def twist(): # to allow the player to pick another card
    print("\nYou twisted") # outputs message on screen
    playerhand.append(dealCard()) # deals player another card
    currenthand() # calls currenthand function to display their cards again
    option() # calls option function to give them a choice again

def gameOver(): # to tell them the game is over
    retry = input("\nWould you like to play again? type yes or no: ") # asks them if they want to try again for them to answer
    if retry == "yes": # if statement, if they answer yes
        print("\n*************************************") # to have a gap between the old game and the new game
        startgame() # calls startgame function to start the game again
    elif retry == "no": # if their answer is no
        print("\nThanks for playing\n") # outputs message on the screen
        quit(0) # the quit function exits the game completly and the 0 in the brackets makes sure the program ends with no errors
    else:
        print("\nInvalid input, try again") # outputed on the screen if their is an error in their input
        gameOver() # calls gameOver function for them to answer again


def startgame(): # allows them to start the game from the beginning
    buildDeck() # calls buildDeck function for them to build the deck again
    playerhand.append(dealCard()) # deals them a card to their hand
    playerhand.append(dealCard()) # deals player another card
    currenthand() # calls currenthand function to display to them their hand
    option() # calls option function to give them the choice to twist or stick
    
startgame()

