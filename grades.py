#exam grade generator

print("Exam Grade Calculator")
print()
name_of_exam = input("Name of exam: ")
print()
total_score = int(input("Max. Possible Score:"))
your_score = int(input("Your score: "))
print()

number_score = float(your_score / total_score)
score = round(number_score, 2)
percentage = round(float(your_score / total_score)*100, 2)

print("You got",percentage,"%")

if score >= .90:
  print("Your letter score is an A+")
elif score >= .80 and score <= .89:
  print("Your letter grade is an A-.")
elif score >= .70 and score <= .79:
  print("Your letter score is a B.")
elif score >= .60 and score <= .69:
  print("Your letter grade is a C.")
elif score >= .50 and score <= .59:
  print("Your letter grade is a D.")
elif score <= .49:
  print("Your letter grade is a F.")
else: 
  print("Try again!")