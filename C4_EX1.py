#Geometry: area of a pentagon
import math

length = float(input("Enter the length from the center to a vertex: "))
s = 2 * length * math.sin(math.pi / 5)
area = (5 * math.pow(s, 2)) / (4 * math.tan(math.pi / 5))

print("The area of the pentagon is {:.2f}".format(area))