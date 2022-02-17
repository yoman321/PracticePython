#Geometry: great circle distance
import math

x1, y1 = [float(x) for x in input("Enter point 1 (latitude and longitude) in degrees: ").split()]
x2, y2 = [float(x) for x in input("Enter point 2 (latitude and longitude) in degrees: ").split()]

radx1 = math.radians(x1)
rady1 = math.radians(y1)
radx2 = math.radians(x2)
rady2 = math.radians(y2)
d = 6371.01 * math.acos(math.sin(radx1) * math.sin(radx2) + math.cos(radx1) * math.cos(radx2) * math.cos(rady1 - rady2))

print("The distance between the two points is {:.2f}".format(d))