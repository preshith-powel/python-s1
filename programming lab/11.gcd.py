
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b:
        a,b=b,a%b
    return a

print("GCD of ",a," and ",b," is ",gcd(a,b))

