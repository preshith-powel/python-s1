dictionary={'name':'presh','age':'21','branch':'mca','hobby':'singing'}
keys=list(dictionary.keys())
keys.sort()
print("ascending order: ")
for key in keys:
    print(f"{key}:{dictionary[key]},",end=" ")
keys.reverse()
print("descending order: ")
for key in keys:
    print(f"{key}:{dictionary[key]},",end=" ")