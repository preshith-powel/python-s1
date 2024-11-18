def calc():
    try:
        while(True):
            a=input("Enter 1st Number: ")
            if a=='exit':
                break
            a=int(a)
            b=int(input("Ënter 2nd Number: "))
            choice=input("Enter the operation:\n (+,-,*,/)")
            if choice == '+':
                c=a+b
                print("Sum= ",c)
            elif choice == '-':
                print("Difference= ",a-b)
            elif choice == '*':
                print("Product= ",a*b)
            elif choice == '/':
                print("Result= ",a/b)
            elif choice=='exit':
                break
            else:
                print("Not defined")
            print("enter 'exit' to exit")
    except:
        print("Invalid input")
        calc()

calc()