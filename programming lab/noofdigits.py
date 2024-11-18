num=int(input("Enter the number: "))
temp=num
count=0
if num==0:
    print("number of digits of number",temp,"is 1")
else:
    while num!=0:
        num=num//10
        count+=1
    print("number of digits of number",temp,"is ",count)