import random
class Mice:
    
    num = []
    guesses = 0
    
    def play(self):
        while True:
            self.digit() #Generates random 4 digit code
            while True:
                 if self.guess():
                    break
            option = input("Do you want to continue playing: ")
            if option == "no":
                 break




    def digit(self):
        self.num = []
        for i in range(0,4):
            self.num.append(random.randint(0,9))
        print(self.num)

    def guess(self):
        mice = 0
        men = 0
        self.guesses += 1
        digitGuess = input("Enter the code you think it is: ")
        for i in range(0,4):
            if self.num[i] == int(digitGuess[i]):
                mice += 1
            elif int(digitGuess[i]) in self.num:
                men +=1
        if mice == 4:
            print(f"you guessed correctly you guessed {self.guesses} number of times")
            return True
        else:
            print(f"wrong code you guessed {mice} correctly and {men} men correctly")
            return False

game = Mice()
game.play()
        