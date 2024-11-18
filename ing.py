string=input("Enter the string: ").lower()
if string[-3:]=='ing':
    print(string+'ly')
else:
    print(string+'ing')