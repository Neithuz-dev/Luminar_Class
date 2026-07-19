char = "ABCDEFBGHCDEHI"
# rep = {}
#
# for i in char:
#     if i not in rep:
#         rep[i]=1
#     else:
#         print(i)
#         break
# print(rep)

rep = {}

for i in char:
    if i in rep:
        print(i)
        rep[i]+=1
        break
    else:
        rep[i]=1
print(rep)
