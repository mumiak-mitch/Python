#Having fun with python
#This programs can generate multiple messages
#Some variable are modified according to the users input
#The message is the same being sent to different people

names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {}, \n\nThis is a reminder that you have {} assignments left to submit before you can graduate. Your current grade is {}, it can increase to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
