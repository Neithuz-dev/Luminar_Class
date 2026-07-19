main_ls=[
    [101,'ajay',25,'bigdata',27000],
[102,'vinay',26,'python',34000],
[103,'vimal',27,'power bi',35000],
[104,'jasmin',54,'engineer',38000],
[105,'Anu',45,'engineer',39000]

]
# for ls in main_ls:
#     age = ls[2]
#     if age > 30:
#         print(ls)
# for ls in main_ls:
    # profe = ls[3]
    # sal = ls[4]
    # if profe == "engineer" and sal >30000:
    #     print(ls[1::])
# sum_sal = 0
# for ls in main_ls:
#     total = ls[4]
#     sum_sal +=total
# print(sum_sal)
#
for ls in main_ls:
    prof = ls[3]
    if prof == "python":
        print(ls[1],ls[3],ls[-1])
