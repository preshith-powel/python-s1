n=int(input("Enter the step: "))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")    
for i in range(n):
    for j in range(n-i-1):
        print("*",end=" ")
    print("\n")