#String concatenation

food = input("Name a food > ")
plant = input("Name a type of plant > ")
cooking = input("Name a method of cooking? > ")
word = input("What word describes burned food? > ")
diy = input("Name a DIY item > ")

print("MENU")
print(cooking + food + " with " + word + plant + " on a bed of " + diy)