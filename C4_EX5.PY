#Geometry: area of a regular polygon
import math

nbreOfSides = float(input("Enter the number of sides: "))
lengthSides = float(input("Enter the length of the side: "))

area = (nbreOfSides * math.pow(lengthSides,2)) / (4 * math.tan(math.pi / nbreOfSides))
print("The area of the polygon is {:.2f}".format(area))