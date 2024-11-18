n=int(input("Enter the step: "))
for i in range(1,n+1):
    k=1
    temp=i
    while temp>0:
        print(i*k,end=" ")
        k+=1
        temp-=1
    print("\n")

