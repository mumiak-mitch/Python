# we can set up the variable, control condition, and increment all in ONE line of code
# Figure out how much you owe altogether for 10 years?

loan = 10000
apr = 0.01
for i in range(10):
  loan+=(loan*apr)
  print("Year", i+1, "is", round(loan,2))