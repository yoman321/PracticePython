#Count positive and negative numbers and compute the average of numbers

num = float(input("Enter an integer, the input ends if it is 0: "))
total = 0
count = 0

while (num != 0):
    total += num
    count += 1
    num = float(input())

if (count == 0):
    print("No numbers are entered except 0")
else:
    average = total / count
    print("The total is {}".format(total))
    print("The average is {}".format(average))
