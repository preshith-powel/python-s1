num=int(input("Enter the number to find the factorial of: "))

def fact(x):
    f=1
    while(x>0):
        f=f*x
        x=x-1
    return f

print("Factorial of ",num," is ",fact(num))
