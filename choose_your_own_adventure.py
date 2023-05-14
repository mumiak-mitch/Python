name = input("What is your name? ")
print("Welcome", name, "to this adventure!")

answer=input("To start, do you want to use the left or right path? ").lower()

if answer == "left":
    answer = input("You have come to the jungle, do you want to go through it or around it? (through/around): ")

    if answer == "through":
        print("You were brave but the lion was braver than you.")
        print("Game over!")
    elif answer == "around":
        print("You walked for so long without food and water, hence you collapsed.")
        print("Game over!")
    else:
        print("Not a valid option, Game over!")

elif answer == "right":
    answer = input("You have come to a village, do you want to go through it or around it? (through/around): ")

    if answer == "through":
        print("Your journey was a success as the village was the safest route.")
        print("Congratulations", name, "you won!")
    elif answer == "around":
        print("You walked for so long without food and water, hence you collapsed.")
        print("Game over!")
    else:
        print("Not a valid option, Game over!")

else:
    print("Not a valid option, Game over!")