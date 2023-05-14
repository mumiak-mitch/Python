#A quiz game that asks questuons
#It ouputs the score and number of questions passed

print("Welcome to my Quiz Game!")

name = input("What is your name? ")
print("Welcome " +name)

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print("central processing unit")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print("graphics processing unit")

answer = input("What does HDD stand for? ")
if answer.lower() == "hard disk drive":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print("hard disk drive")

answer = input("What does SDD stand for? ")
if answer.lower() == "solid state drive":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print("solid state drive")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print("solid state drive")

print("You got " + str(score) + " questions correct!")
print("You scored " + str((score / 5) * 100) + " %.")