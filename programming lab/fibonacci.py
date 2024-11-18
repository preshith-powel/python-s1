n=int(input("Enter the number of terms of the fibonacci series: "))
print("0,1",end=",")
a=0
b=1
while n>0:
    c=a+b
    print(c, end=",")
    n=n-1
    a,b=b,c