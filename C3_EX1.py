#Algebra: solve quadratic equations
import math

a, b, c = [float(x) for x in input("Enter a, b, c: ").split()]
discriminant = float(math.pow(b, 2) - 4 * a * c)

if discriminant > 0:
    r1 = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
    r2 = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
    print("The equation has two roots", r1,"and", r2)
elif discriminant ==  0:
    r1 = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
    print("The equation has one root", r1)
else:
    print("The equation has no roots")
