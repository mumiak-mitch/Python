#Positive affirmation program

print("Positive affirmations")
print()

name = input("Who are you? ")
print()

achieve = input("What do you want to achieve today? ")
print()

mood =  input("On a scale of 1 - 10 how do you feel today? ")
print()

if mood == "1" or "2" or "3":
  print("Hey ", name, "despite the fact that you feel low don't let it ruin your day. Accept yourself the way you are and take care of yourself.")
  print("Success, as you embark on: ")
  print(achieve)
elif mood == "4" or "5" or "6":
  print("Hey ", name, "I know you feel confused but just relax and take care of your shit")
  print("Success, as you embark on: ")
  print(achieve)
elif mood == "7" or "8" or "9":
  print("Hey ", name, "you seem to be in a great mood today please do remember to create an impact to society")
  print("Success, as you embark on: ")
  print(achieve)
elif mood == "10":
  print("Hey ", name, "you have discovered the secret of happiness. Hurray!")
  print("Success, as you embark on: ")
  print(achieve)
else:
  print("Sorry for the bitterness")
  print()
  
print("Thanks for the feedback")
print("Have a nice day")      