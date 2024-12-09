class Publisher():
    def __init__(self, name='name'):
        self.name=name

    def class_definition(self):
        print("This is the publisher class.")

class Book(Publisher):
    def __init__(self, name='name', title='title', author='author'):
        super().__init__(name)
        self.title=title
        self.author=author
        
class Python(Book):
    def __init__(self, name='name', title='title', author='author',price='0',noofpages='0'):
        super().__init__(name, title, author)
        self.price=price
        self.noofpages=noofpages

    def getInfo(self):
        print(
            f"Book Name: {self.name}\nTitle: {self.title}\nAuthor:{self.author}\nPrice:{self.price}\nNo. of pages:{self.noofpages}"
        )
    
    def class_definition(self):
        print("This is the python class.")

if __name__=="__main__":
    name=input("What is the name of the book: ")
    title=input("What is the title of the book: ")
    author=input("Who is the author of the book: ")
    price=input("What is the price of the book: ")
    noofpages=input("Enter the number of pages: ")
    pythonbook=Python(name,title,author,price,noofpages)
    pythonbook.getInfo()

    #Example of method overriding
    publisher=Publisher()
    book=Book()
    publisher.class_definition()
    book.class_definition()
    pythonbook.class_definition()