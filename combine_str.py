string1=list(input("Enter the first string: "))
string2=list(input("Enter the second string: "))
temp=string1[1]
string1[1]=string2[1]
string2[1]=temp
print(''.join(string1)+"".join(string2))