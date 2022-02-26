#Sort three numbers
def displaySortedNumbers(num1, num2, num3):
    if num2 < num1 and num2 < num3:
        temp = num1
        num1 = num2
        num2 = temp
    if num3 < num1 and num3 < num2:
        temp = num1
        num1 = num3
        num3 = temp
    if num3 < num2:
        temp = num3
        num3 = num2
        num2 = temp
    if num2 < num1:
        temp = num2
        num2 = num1
        num1 =  temp
    
    print("The increasing order of these numbers is: {} {} {}".format(num1, num2, num3))

num1, num2, num3 = [int(x) for x in input("Input three numbers: ").split()]
displaySortedNumbers(num1, num2, num3)

