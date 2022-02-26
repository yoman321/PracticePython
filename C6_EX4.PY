#Display an integer reversed
def reverse(number):
    temp = 0
    while (number != 0):
        temp = int(temp * 10 + number % 10)
        number = int(number / 10)
    
    return temp

number = int(input("Enter a number: "))
print("The reverse of {} is {}".format(number, reverse(number)))
