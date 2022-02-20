#Repeat additions
import time
import random

startTime = time.time()
count = 1
rightAnswer = 0

while count <= 10:
    num1 = random.randrange(1, 16, 1)
    num2 = random.randrange(1, 16, 1)

    if num1 < num2:
        num1, num2 = num2, num1
    
    answer = int(input("What is {} - {}? ".format(num1, num2)))

    if num1 - num2 == answer:
        print("You are correct!\n")
        rightAnswer += 1
    else:
        print("Your answer is wrong.")
        print("{} - {} should be {}\n".format(num1, num2, num1 - num2))
    
    count += 1

endTime = time.time()
print("Correct count is {}".format(rightAnswer))
print("Test time is {}".format(endTime - startTime))
