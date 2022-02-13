#Compute the volume of a cylinder
import math

print("Enter the radius and length of a cyllinder: ")
radius, length = [float(x) for x in input().split()]

area = radius * radius * math.pi
volume = area * length
print("The area is ",area)
print("The volume is ",volume)  