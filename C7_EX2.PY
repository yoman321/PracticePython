#Reverse the numbers entered
numString = input("Input 10 numbers: ")
numList = numString.split(" ")

numList.reverse()
for i in range(len(numList)):
    print(numList[i], end = " ")