#Assign grades
numStudents = input("Enter the number of students: ")
scoreString = input("Input {} scores: ".format(numStudents))

scoreList = scoreString.split()
best = 0
for i in range(len(scoreList)):
    scoreList[i] = int(scoreList[i])
    if (scoreList[i] > best):
        best = int(scoreList[i])

for i in range(len(scoreList)):
    if (int(scoreList[i]) >= best - 10):
        print("Student {}  score is {} and grade is A".format(i, scoreList[i]))
    elif (int(scoreList[i]) >= best - 20):
        print("Student {} score is {} and grade is B".format(i, scoreList[i]))
    elif (int(scoreList[i]) >= best - 30):
        print("Student {} score is {} and grade is C".format(i, scoreList[i]))
    else:
        print("Student {} score is {} and grade is D".format(i, scoreList[i]))