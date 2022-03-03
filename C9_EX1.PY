#The Rectangle class
class Rectangle:
    width = 1
    height = 1
    def __init__(self):
        Rectangle.width = 1
        Rectangle.height = 1
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height
    def getPerimeter(self):
        return 2 * self.width + 2 * self.height

r1 = Rectangle(4, 40)
r2 = Rectangle(3.5, 35.9)

print("The width is {}, height is {}, area is {}, and perimeter is {} for rectangle r1.".format(r1.width, r1.height, r1.getArea(), r1.getPerimeter()))
print("The width is {}, height is {}, area is {:.2f}, and perimeter is {} for rectangle r2.".format(r2.width, r2.height, r2.getArea(), r2.getPerimeter()))
