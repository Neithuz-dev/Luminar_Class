char = "ABCDEFBGHCDEHI"
rep = {}

for i in char:
    if i not in rep:
        rep[i]=1
    else:
        print(i)
        break
print(rep)
