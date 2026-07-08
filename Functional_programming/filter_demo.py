ls = [6,7,8,9,10,20,3,4]

ele_6 = tuple(filter(lambda x:x>6,ls))
print(ele_6)

even_ls = list(filter(lambda x:x%2==0,ls))
print(even_ls)

add_ls = list(map(lambda x:x+5,ls))
print(add_ls)

gr_5 = list(filter(lambda x:x<5,ls))
print(gr_5)

odd_ls = list(filter(lambda x:x%2!=0,ls))
cube = list(map(lambda x:x**3,odd_ls))
print(cube)