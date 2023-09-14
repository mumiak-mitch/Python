#How many seconds are in a year?

leap = input('Is it a leap year?\n\tY/N:\t')
if leap.lower() == 'y' or leap.lower() == 'yes' or leap.lower() == 'ye':
  seconds = 60 * 60 * 24 * 31 * 12
  print('60 Seconds in 1 Minute\n\n60 Minutes in 1 hour\n\n24 Hours in 1 Day\n\n29-31 Days in a year!\n\n12 Months in 1 Year So',seconds,'seconds in a year')
elif leap.lower() == 'n' or leap.lower() == 'no' or leap.lower() == 'na':
  seconds = 60 * 60 * 24 * 30 * 12
  print('60 Seconds in 1 Minute\n\n60 Minutes in 1 hour\n\n24 Hours in 1 Day\n\n28-30 Days in a year!\n\n12 Months in 1 Year\n\n So',seconds,'seconds in a year')
else:
  print('Math seems to be your enemy')