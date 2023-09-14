# However, sometimes we might want to take part of a string to use it somewhere else. 
#Sometimes, we might want to look at just the first letter of a string or chop it into chunks.
#To do this, we use string slicing.
#To slice a single character from a string, you use the index of that character in square brackets [] 

print("STAR WARS NAME GENERATOR")

all = input("Enter your first name, last name, Mum's maiden name and the city you were born in ").split()

first = all[0].strip()
last = all[1].strip()
maiden = all[2].strip()
city = all[3].strip()

name = f"{first[:3].title()}{last[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"

print(f"Your Star Wars name is {name}")