class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height=height
        self.area=0
        self.perimeter=0
    
    def getArea(self):
        self.area= self.width * self.height
    
    def getPerimeter(self):
        self.perimeter = 2 * (self.width + self.height)
    
if __name__=="__main__":
    width1=int(input("Enter the width of 1st rectangle : "))
    height1=int(input("Enter the height of 1st rectangle : "))
    width2=int(input("Enter the width of 2nd rectangle : "))
    height2=int(input("Enter the height of 2nd rectangle : "))
    rect1=Rectangle(width1,height1)
    rect2=Rectangle(width2,height2)
    rect1.getArea()
    rect2.getPerimeter()
    if rect1.area>rect2.area:
        print("The area of rectangle 1 is greater than rectangle 2")
    elif rect1.area<rect2.area:
        print("The area of rectangle 2 is greater than rectangle 1")
    else:
        print("Both rectangles have equal area")
