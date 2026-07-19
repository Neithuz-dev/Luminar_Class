ls = [9,9,8,7,5,4,3,2,1,1,6,7,8,9]
new_ls = []
for i in ls:
    if i not in new_ls:
        new_ls.append(i)
print(new_ls)