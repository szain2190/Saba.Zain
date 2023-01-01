# TEXT ADVENTURE

# KEY POINTS
# take inputs
# conditional statements if, else if, and else
# functions

name = ""
# variable to store the players name

def start():
  # start of the game. choice of left or right door
  print(f"\nWelcome to castle escape {name}!")
  # welcome message to welcome the player into the game
  print(f"\n{name} you wake up on the floor and your stuck in a castle there are two doors in the room left and right the aim of the game is to get out of the castle without the guards\nfinding or noticing you, otherwise you will end up in the castle dungeons.")
  # a little of the story so the user knows what the game is about
  door = input("\nChoose a door type left or right: \n")
  # user inputs their choice
  if door == "left": # if statement calls the function depending on their input
    leftDoor() # if the player types left it calls the leftDoor function
  elif door == "right":
    rightDoor() # otherwise if the player types right  it calls the rightDoor function
  else:
    print("\nInvalid input try again")
    # error statement is displayed if they put an input that is not recognised 
    start()
    # start function is called to give them a chance to start the game again
  
  

 
def leftDoor():
  print("\nYou chose the left door, there is a dragon you can either: creep past the dragon, fight the dragon or try the right door instead.\n")
  # left door function, displays a message to tell you what is behind the left door 
  choice1 = input("\nChoose an option either creep, fight or right: \n")
  # player enters their choice
  if choice1 == "creep": # if statement calls the function depending on their input
    creep() # if player types creep the creep function is called
  elif choice1 == "fight":
    fight() # if they type fight the fight function is called
  elif choice1 == "right":
    rightDoor() # otherwise if they choose right the rightDoor function is called
  else:
    print("\nInvalid input, try again")
    # error statement is displayed if they put an input that is not recognised
    leftDoor()
    # left door function is called if the input is not recognised so they can try again
  

  
def rightDoor():
  print("\nYou chose the right door, the room is flooded you can either: swim through the room, pull the plug to let all the water out or you can choose the left door instead\n")
  # right door function, displays a message to tell you what is behind the right door
  choice2 = input("\nChoose an option either swim, plug or left: \n")
  # player enters their choice
  if choice2 == "swim": # if statement calls the function depending on their input
    swim() # if they type swim the swim function is called
  elif choice2 == "plug":
    plug() # if they type plug the plug function is called
  elif choice2 == "left":
    leftDoor() # otherwise if they choose left the leftDoor function is called
  else:
    print("\nInvalid input, try again")
    # error statement is displayed if they put an input that is not recognised
    rightDoor()
    # right door function is called if the input is not recognised so they can try again



def swim():
  print("\nYou swam through the water and made it to the other side.\nYou open the door and see a guard standing there with a key in his pocket, the key to escape the castle, but opposite the guard is another room.\nYou can either take the key off the guard or go into the mystery room.\n")
  # swim function, displays a message to tell you what you can do next
  choice3 = input("Choose an option type either take or room: \n")
  # player enters their choice
  if choice3 == "take": # if statement calls the function depending on their input
    take() # if they type take the take function is called
  elif choice3 == "room": 
    mysteryRoom() # otherwise if they type room the mysteryRoom function is called
  else:
    print("\nInvalid input, try again")
    # error statement is displayed if they put an input that is not recognised
    swim()
    # swim function is called if the input is not recognised so they can try again



def take():
  print("\nThat was a bad idea you tried to run but the guard caught you and took you to the castle dungeons")
  # take function, displays a message to tell you what has happened with your choice
  gameOver()
  # gameOver function is called




def mysteryRoom():
  print("\nYou go into the mystery room and you have to try and find something to knock the guard out with so you can take the key.\nThere is the choice of a sleeping potion or a tranquilizer dart gun.")
  # mystery room function, displays a message to tell you what you can do next
  choice6 = input("\nChoose either one, type potion or dart: \n")
  # player enters their choice
  if choice6 == "potion": # if statement calls the function depending on their input
    potion() # if they type potion the potion function is called
  elif choice6 == "dart":
    dart() # otherwise if they type dart the dart function is called
  else:
    print("\nInvalid input, try again")
    # error statement is displayed if they put an input that is not recognised
    mysteryRoom()
    # mysteryRoom function is called if the input is not recognised so they can try again




def dart():
  print("\nYou tried to fire the gun at the guard to put him to sleef but ot was out of darts.\nThe guard took you to the castle dungeons.")
  # dart function, displays a message to tell you what has happened with your choice
  gameOver()
  # gameOver function is called


def potion():
  print("\nYou grab the potion and throw it at the guard putting him to sleep.\nYou take the key out of his pocket and open the door.\n\nYou are now outside seeing two separate paths you have to choose left or right.")
  # potion function, displays a message to tell you what you can do next
  choice7 = input("\nChoose either one, type left or right: \n")
  # player enters their choice
  if choice7 == "left": # if statement calls the function depending on their input
    leftPath() # if they type left the leftPath function is called
  elif choice7 == "right":
    rightPath() # otherwise if they type right the right function is called
  else:
    print("\nInvalid input, try again")
    # error statement is displayed if they put an input that is not recognised
    potion()
    # potion function is called if the input is not recognised so they can try again




def leftPath():
  print("\nYou chose the left path leading to your house.\n\nYou escaped and won!")
  # leftPath function, displays a message to tell you what has happened with your choice
  gameOver()
  # gameOver function is called




def rightPath():
  print("\nThat was a bad idea the path lead you to the forest were you could not find your way out and got eaten by a bear.")
  # rightPath function, displays a message to tell you what has happened with your choice
  gameOver()
  # gameOver function is called



def plug():
  print("\nThat was a bad idea it took too long for all of the water to drain out and the guard caught you and took you to the castle dungeons")
  # plug function, displays a message to tell you what has happened with your choice
  gameOver()
  # gameOver function is called




def creep():
  print("\nYou creep past the dragon and get to the other side of the room without him noticing.\nYou open the door and find a zipwire and an elevator and at the bottom you see a guard with a key in his pocket.\nYou can choose to take either one of them to try and escape.")
  # creep function, displays a message to tell you what you can do next
  choice4 = input("\nChoose an option type either zipwire or elevator: \n")
  # player enters their choice
  if choice4 == "zipwire": # if statement calls the function depending on their input
    zipwire() # if they type zipwire the zipwire function is called
  elif choice4 == "elevator":
    elevator() # otherwise if they type elevator the elevator function is called
  else:
    print("\nInvalid input try again")
    # error statement is displayed if they put an input that is not recognised
    creep()
    # creep function is called if the input is not recognised so they can try again




def zipwire():
  print("\nYou took the zipwire down and you knocked out the guard.\nYou take the key from his pocket and open the door.\n\nYou are now outside, to your left you see the stables with the horses, and to your right you see a car that is already started.\nYou can choose to take the car or a horse.")
  # zipwire function, displays a message to tell you what you can do next
  choice5 = input("\nChoose an option type either horse or car: \n")
  # player enters their choice
  if choice5 == "horse": # if statement calls the function depending on their input
    horse() # if they type horse the horse function is called
  elif choice5 == "car":
    car() # otherwise if they type car the car function is called
  else:
    print("\nInvalid input, try again")
    # error statement is displayed if they put an input that is not recognised
    zipwire()
    # zipwire function is called if the input is not recognised so they can try again




def horse():
  print("\nYou jumped on a horse and rode out of the castle.\nThe horse was too fast and the other guards could not catch you up.\n\nYou escaped and won!")
  # horse function, displays a message to tell you what has happened with your choice
  gameOver()
  # gameOver function is called




def car():
  print("\nYou got in the car and started to drive out of the castle, with the guards following you behind trying to catch you.\nThe car eventually ran out of petrol and the guards catch you and take you to the dungeons.")
  # car function, displays a message to tell you what has happened with your choice
  gameOver()
  # gameOver function is called




def elevator():
  print("\nThat was a bad idea, you pressed the button to the elevator and while you were waiting the guard caught sight of you and took you to the castle dungeons.")
  # elevator function, displays a message to tell you what has happened with your choice
  gameOver()
  # gameOver function is called




def fight():
  print("\nThat was a bad idea you got eaten")
  # fight function, displays a message to tell you what has happened with your choice
  gameOver()
  # gameOver function is called




def gameOver():
  print("\nGame over")
  # displays message once game is over
  retry = input("\nWould you like to try again? Type yes or no: \n")
  # player enters their choice if they want to play again
  if retry == "yes": # if statement calls the function depending on their input
    start() # if they type yes the start function is called
  elif retry == "no":
    finished() # otherwise if they type no the finished function is called
  else:
    print("\nInvalid input, try again")
    # error statement is displayed if they put an input that is not recognised
    gameOver()
    # gameOver function is called




def finished():
  print("\nGame finished\n")
  # displays message if the player does not want to play again

name = input("\nEnter your name: \n")
# allows the player to enter their name before the start of the game 
start()
# calls start function to start the game