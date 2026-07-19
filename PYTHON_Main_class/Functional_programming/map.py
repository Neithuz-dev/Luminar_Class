ls = [5,6,7,8,9]
sq_ls = []
for i in ls:
    sq_ls .append(i**2)
print(sq_ls)

sql_ele = tuple(map(lambda x:x**2,ls))
print(sql_ele)