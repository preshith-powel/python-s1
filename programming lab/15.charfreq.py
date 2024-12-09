string=input("Enter the string: ").lower()
string=string.strip()
string=string.replace(" ","")
string2=set(string)

for char in string2 :
    c=0
    for i in string:
        if char==i:
            c+=1
    print("number of ",char,"is",c)