#A program that takes age as input and determines the category it belongs to

age = int(input('Please enter your age: '))

if age > 0 and  age < 18:
    print('You are a minor')
elif age > 18 and age < 65:
    print('You are an adult.')
elif age >= 65:
    print('You are a senior.')
else:
    print('Invalid')

print(age)