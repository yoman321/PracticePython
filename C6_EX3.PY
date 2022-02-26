#Palindrom Integer
def isPalindrome(number):
    temp = 0
    while (temp < number):
        temp = int(temp * 10 + number % 10)
        number = int(number / 10)

    if (number == temp or number == int(temp / 10)):
        return True

    return False

number = int(input("Input an integer: "))
if (isPalindrome(number)):
    print("This number is a palindrome")
else:
    print("This number is NOT a palindrome")
