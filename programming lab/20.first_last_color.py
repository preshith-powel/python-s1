colors=input("Enter the colors:").split(",")
for i in range(len(colors)):
    colors[i]=colors[i].strip()
    if not colors[i]:
        del colors[i]
print(f"First color is: {colors[0]};\n Last color is: {colors[-1]}")