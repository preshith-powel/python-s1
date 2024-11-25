dictionary1={}
dictionary2={}
num_dict1=int(input("Enter the number of key value pairs for the first dictionary: "))
for i in range(num_dict1):
    key=input("Enter the key for the first dictionary: ")
    value=input("Enter the value for the first dictionary: ")
    dictionary1[key]=value
num_dict2=int(input("Enter the number of key value pairs for the second dictionary: "))
for i in range(num_dict2):
    key=input("Enter the key for the second dictionary: ")
    value=input("Enter the value for the second dictionary: ")
    dictionary2[key]=value
dictionary3={}
dictionary3.update(dictionary1)
dictionary3.update(dictionary2)
print("merged dictionary:\n",dictionary3)
