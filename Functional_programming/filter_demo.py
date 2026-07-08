ls = [6,7,8,9,10,20,3,4]

ele_6 = tuple(filter(lambda x:x>6,ls))
print(ele_6)

even_ls = list(filter(lambda x:x%2==0,ls))
print(even_ls)

add_ls = list(map(lambda x:x+5,ls))
print(add_ls)

gr_5 = list(filter(lambda x:x<5,ls))
print(gr_5)


cube = list(map(lambda x:x**3,filter(lambda x:x%2!=0,ls)))
print(cube)

mul_10 = list(map(lambda x: x*10,filter(lambda x:x>5,ls)))
print(mul_10)

sqr_num = list(map(lambda x: x**2,filter(lambda x:x>5,ls)))
print(sqr_num)