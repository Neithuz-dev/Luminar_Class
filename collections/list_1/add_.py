old_ls = [15,3,10,6,9,7]
# total  = 0
# new_ls = []
# for i in old_ls:
#     total +=i
# for i in old_ls:
#     new_ls.append(total-i)
# print(new_ls)
total  = sum(old_ls)
new_ls = []
for i in old_ls:
    new_ls.append(total - i)
print(new_ls)