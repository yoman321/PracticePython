#Analyze scores
inputString = input("Enter a maximum of 100 scores. A negative score ends the input: ")
nums = inputString.split()

sum = 0
length = 0
for i in range(len(nums)):
    if int(nums[i]) < 0:
        length = i
        break
    sum += int(nums[i])

average = int(sum / length)

countNeg = 0
countPos = 0
for i in range(length):
    if int(nums[i]) >= average:
        countPos += 1
    else:
        countNeg += 1

print("The average is {}. There are {} score above the average and there are {} score below the average.".format(average, countPos, countNeg))