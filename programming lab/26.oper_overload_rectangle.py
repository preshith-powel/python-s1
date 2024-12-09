class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width=width
        self.__height=height

    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height

    def getArea(self):
        return self.__width*self.__height
    
    def __lt__(self,other):
        if self.getArea()>other.getArea():
            return "rectangle A has the greater area"
        elif self.getArea()==other.getArea():
            return "Areas are the same!"
        else:
            return "rectangle B has the greater area"

if __name__=="__main__":
    width1=int(input("Enter the width of rectangle A: "))
    height1=int(input("Enter the height of rectangle A: "))
    width2=int(input("Enter the width of rectangle B: "))
    height2=int(input("Enter the height of rectangle B: "))
    rect1=Rectangle(width1,height1)
    rect2=Rectangle(width2,height2)
    greater=rect1<rect2
    print(greater)