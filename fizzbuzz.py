#Checks whether a number is divisible by 3 or 5 and resonds with fizz or buzz

for num in range(1,21):
    string = ''
    if num % 3 == 0:
        string = string + 'Fizz'
    if num % 5 == 0:
        string = string + 'Buzz'
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string)