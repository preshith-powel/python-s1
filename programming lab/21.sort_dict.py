dictionary={}
num_dict=int(input("Enter the number of key value pairs you want to enter: "))
for i in range(num_dict):
    key=input("Enter the key: ")
    value=input("Enter the value: ")
    dictionary[key]=value
keys=list(dictionary.keys())
keys.sort()
print("ascending order: ")
for key in keys:
    print(f"{key}:{dictionary[key]},",end=" ")
keys.reverse()
print("descending order: ")
for key in keys:
    print(f"{key}:{dictionary[key]},",end=" ")