from graphics import circle, rectangle
from graphics.three_dgraphics.cuboid import *
from graphics.three_dgraphics.sphere import *

radius=int(input("Enter the radius of the circle you want to find area and perimeter of: "))
print("Area of circle: ",circle.circle_area(radius))
print("Perimeter of circle: ",circle.circle_perimeter(radius))

length=int(input("Enter the length of the rectangle you want to find the area and perimeter of: "))
breadth=int(input("Enter the breadth of the rectangle you want to find the area and perimeter of: "))
print("Area of rectangle: ",rectangle.rectangle_area(length,breadth))
print("Perimeter of rectangle: ",rectangle.rectangle_perimeter(length,breadth))

radius=int(input("Enter the radius of the sphere you want to find area and perimeter of: "))
print("Area of sphere: ",sphere_area(radius))
print("Perimeter of sphere: ",sphere_perimeter(radius))

length=int(input("Enter the length of the cuboid you want to find the area and perimeter of: "))
breadth=int(input("Enter the breadth of the cuboid you want to find the area and perimeter of: "))
height=int(input("Enter the height of the cuboid you want to find the area and perimeter of: "))
print("Area of cuboid: ",cuboid_area(length,breadth,height))
print("Perimeter of cuboid: ",cuboid_perimeter(length,breadth,height))
