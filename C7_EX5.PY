#Print distinct numbers
distinctDict = {

}
inputString = input("Enter 10 numbers: ")
nums = inputString.split()

for i in nums:
    if not i in distinctDict:
        distinctDict[i] = i

print("The distinct numbeers are: ", end = "")
for i in distinctDict:
    print(i, end=" ")
