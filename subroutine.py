#A subroutine tells the computer that a piece of code exists and to go run that code again and again...

def login():
  while True:
    username = input("What is your username?: ")
    password = input("What is your password? ")
    if username == "David" and password == "123456789":
      print("Welcome David!")
      break
    else:
      print("That is not the correct username or password. Try again!")
      continue
    
print("Login")
print()
login()