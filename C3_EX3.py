#Algebra: solve 2 x 2 linear equations

a, b, c, d, e, f = [float(x) for x in input("Enter a, b, c, d, e, f: ").split()]
denominator = a * d - b * c

if (denominator == 0):
    print("The equation has no solution")
else:
    x = (e * d - b * f) / denominator
    y = (a * f - e * c) / denominator
    print("x is {} and y is {}".format(x, y))