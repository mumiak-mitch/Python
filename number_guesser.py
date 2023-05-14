#A program that prompts the user to guess a number
#It checks if the user is correct

import random

print("Welcome, lets play!")
name = input("What is your name? ")

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

#you can also use randrange instead of randint
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1

    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print('Congratulations,', name,  'you got it right.')
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it right after", guesses, "guesses.")