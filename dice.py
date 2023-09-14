#In a subroutine, the () are for the argument (FYI argument is another word for parameter). 
#These are the pieces of information we pass to the code. These can be variable names that 
#are made up for the first time within the argument ().

import random
print("Infinity Dice")
print()

sides = int(input("How many sides?: "))
playGame = "yes"
  
def rollDice(sides):
  print("You rolled ", random.randint(1,sides))
while playGame == "yes":
    rollDice(sides)
    playGame = input("Roll again?")