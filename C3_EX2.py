#Game: add three numbers
import time

num1 = int(time.time() % 10)
num2 = int(time.time() / 7 % 10)
result = num1 + num2

input = int(input("What is {} + {}? ".format(num1, num2)))
if input == result:
    print(num1, "+", num2, "=", input, "is true")
else:
    print(num1, "+", num2, "=", input, "is false")