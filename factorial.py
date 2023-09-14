#Recursion is a type of program where you get a subroutine to call itself

#Write a function that:
#Starts at the highest number.
#Multiplies that by factorial of itself minus one
#Terminates when it reaches 1 and returns 1
#Outputs the factorial.

def factorial(value):
  if value == 1:
    return 1
  else:
    return value * factorial(value-1)

print(factorial(5))