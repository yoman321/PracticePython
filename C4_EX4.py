#Geometry: area of a hexagon
import math

s = float(input("Enter the side: "))
area = (6 * math.pow(s,2)) /  (4 * math.tan(math.pi/6))
print("The area of the hexagon: {:.2f}".format(area))