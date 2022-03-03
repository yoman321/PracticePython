#Count occurences of numbers
#Instead of looping through the array multiple time as intended, we make a dictionary which have better time complexitty, but yields a different ordering in the answer
numsDict = {

}
inputString = input("Enter the integers between 1 and 100: ")
nums = inputString.split(" ")

for i in range(len(nums)):
    if int(nums[i]) == 0:
        break
    if nums[i] in numsDict:
        # numsDict.update({nums[i]: numsDict.get(nums[i]) + 1})
        numsDict[nums[i]] = numsDict[nums[i]] + 1
    else:
        numsDict[nums[i]] = 1

for x in numsDict:
    if (numsDict[x] > 1):
        print("{} occurs {} times".format(x, numsDict[x]))
    else:
        print("{} occurs {} time".format(x, numsDict[x]))