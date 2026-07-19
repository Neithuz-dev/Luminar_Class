file = open("numbers","r")
ls = []
for i in file:
    ls.append(int(i))
print(ls)
print(sum(ls))