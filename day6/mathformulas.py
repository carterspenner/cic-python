"""
Author: Carter Spenner
Date: 3/30/2026
Purpose: To practice using functions
"""

import math
placeholder = "placeholder"

def rectangleArea(length, width):
    return round(length * width, 2)

def rectanglePerimeter(length, width):
    return round(2 * (length + width), 2)

def rectangularPrismVolume(length, width, height):
    return round(length * width * height, 2)

#90% code

def circleCircumference(radius):
    return round(2 * math.pi * radius, 2)

def circleArea(radius):
    return round(math.pi * radius ** 2, 2)

def sphereVolume(radius):
    return round((4/3) * math.pi * radius ** 3, 2)

#100% code
def trapezoidArea(base1, base2, height):
    return round(((base1 + base2) / 2) * height, 2)

def cylinderVolume(radius, height):
    return round(math.pi * radius ** 2 * height, 2)

#test the functions

print("Rectangle Area:", rectangleArea(5, 3))
print("Rectangle Perimeter:", rectanglePerimeter(5, 3))
print("Rectangular Prism Volume:", rectangularPrismVolume(5, 3, 2))
print("Circle Circumference:", circleCircumference(4))
print("Circle Area:", circleArea(4))
print("Sphere Volume:", sphereVolume(4))
print("Trapezoid Area:", trapezoidArea(5, 3, 4))
print("Cylinder Volume:", cylinderVolume(4, 5))