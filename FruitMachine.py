import random
#5 Fruit Machine
class FruitMachine():
    credit = 100
    symbols = ["Cherry", "Bell", "Lemon", "Orange", "Skull"]
    display = []

    def __init__(self): #__init__ function is called when an object is instantiated
        self.play()

    def play(self): #Controls the flow of the program
        print("***Welcome to the fruit machine!***\n")
        while True: #The game loop, the game continues until we reach a 'break'
            print(f"You have {self.credit} credits")
            if self.credit <= 0: #if the player is out of credits, end the game by breaking out the loop
                print("You've run out of money :(")
                break
            option = input("20 credits to spin! Type 'p' to play or 'q' to quit\n") #option to play or quit
            if option == "p": #if play chosen, deduct 20 credits and call the roll and eval functions
                self.credit -= 20
                self.roll()
                self.eval()
            elif option =="q":
                break
        print("    ***Thanks for playing!***") #After game loop finishes, give a goodbye message


    def roll(self): #roll function update the display list to 3 random symbols after a spin
        self.display.clear()
        print("\n    You rolled:\n")
        print("--", end=" ")
        for i in range(3): #loop 3 times choosing a random item from the symbols list and add it to the display list
            sym = random.choice(self.symbols)
            self.display.append(sym)
            print(sym, end = " -- ")
        print("\n")

    def eval(self): #eval function check the display list for the outcome of the spin
        if self.display.count("Skull") == 3:
            self.credit = 0
            print("Oh no three skulls! You lose all your credits!\n")
        elif self.display.count("Skull") == 2:
            self.credit -= 100
            print("Oh no two skulls! You lose 100 credits!\n")
        elif self.display.count("Bell") == 3:
            self.credit += 500
            print("Jackpot! You win 500 credits!\n")
        elif self.display.count("Cherry") == 3 or self.display.count("Lemon") == 3 or self.display.count("Orange") == 3:
            self.credit += 100
            print("Jackpot! You win 100 credits!\n")
        elif self.display.count("Cherry") == 2 or self.display.count("Bell") == 2 or self.display.count("Lemon") == 2 or self.display.count("Orange") == 2:
            self.credit += 50
            print("Two of the same! You win 50 credits!\n")
        else:
            print("You got nothing....\n")



fm = FruitMachine() #make an instantance of a fruitmachine
