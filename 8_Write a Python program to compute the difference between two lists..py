a=["red", "orange", "green", "blue", "white"]
b=["black", "yellow", "green", "blue"]

c=[]

for e in a:
    if e not in b:
        c.append(e)
print(c)