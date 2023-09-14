#Tip calculator: let's split the bill

print("Tip Calculator")
print()

spend = input(int("How much did you spend? "))
percentage = input(int("What percentage do you want to tip? "))
people = input(int("How many people are in your group? "))
print()

bill = (spend * (percentage/100)) / people
print("You each owe ", )