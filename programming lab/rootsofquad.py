from math import sqrt

a, b, c=map(int,input("Enter the coefficients of the quadratic equations: ").split())
print("The quadratic equation you provided is: ",a,"x^2 + ",b,"x + ",c)
discriminant=b**2 - 4*a*c
if discriminant == 0:
    print("The equation has one real root: ",-b/(2*a))
elif discriminant<0:
    discriminant*=-1
    root1=f"{-b/2*a}+{sqrt(discriminant)/2*a}" 
    root2= f"{-b/2*a}-{sqrt(discriminant)/2*a}"
    print("The equation has two imaginary roots: ",root1,"i,",root2,"i")
else:
    root1= (-b+sqrt(discriminant))/2*a
    root2= (-b-sqrt(discriminant))/2*a
    print("The equation has two real roots, ",root1,",",root2)