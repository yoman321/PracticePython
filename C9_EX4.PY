#Use the Random class
import random

random.seed(1000)

for i in range(50):
    num = random.randrange(1, 100, 1)
    if i % 10 == 0:
        print()
        print(num, end=" ")
    else:
        print(num, end=" ")
