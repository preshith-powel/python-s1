noevenlist=[]
even=map(int,input("Enter items of the list: ").split(" "))
evenlist=list(even)
print("Your list is: ",evenlist)
for i in evenlist:
    if i%2==0:
        pass
    else:
        noevenlist.append(i)
print("List with even numbers removed: ",noevenlist)