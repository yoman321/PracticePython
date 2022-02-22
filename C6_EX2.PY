#Sum the digits in an integer
def sumDigits(digit):
    sum = 0
    while (digit != 0):
        sum += digit % 10
        digit = digit / 10
    
    return int(sum)

digit = int(input("Input a digit: "))
sum = sumDigits(digit)
print("The sum of the digits is {}".format(sum))