#Casting is where we explicitly tell the computer that what we are typing is a number and not a letter.

print("Generation Identifier")
print()

year = input("Which year were you born? ")
print()

if year >= "1883" and year <= "1900":
  print("Lost generation")
elif year >= "1901" and year <= "1927":
  print("Greatest generation")
elif year >= "1928"  and year <= "1945":
  print("Silent generation")
elif year >= "1946"  and year <= "1964":
  print("Baby boomers")
elif year >= "1965"  and year <= "1980":
  print("Generation x")
elif year >= "1981" and year <= "1996":
  print("Millenials")
elif year >= "1997" and year < "2012":
  print("Generation z")
elif year >= "2012":
  print("Generation to alpha")
else:
  print("Unrecognized year")

print("Have a nice day!")