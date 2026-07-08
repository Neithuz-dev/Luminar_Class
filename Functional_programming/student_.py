marks = [45,82,91,68,37,78]

new_mark = list(map(lambda x: "A grade "
            if x>=90 else "B grade"
            if x>=75  else "Cgrade" ,
                    filter(lambda  x:x>=50,marks)))
print(new_mark)

cube_= list(map(lambda x:x**3, filter(lambda x:x%3 == 0, marks)))
print(cube_)

even_100 = list(map(lambda x:x+100,filter(lambda x:x%2==0,marks)))
print(even_100)

ls= [9,7,4,5,2,1,7,6]
num = list(filter(lambda x:x>3 and x<5,ls))
print(num)

sub_2 = list(map(lambda x:x-2,filter(lambda x:x>4,ls)))
print(sub_2)

div_num = list(map(lambda x:x/2,ls))
print(div_num)

sub_3 = list(map(lambda x:x-3,ls))
print(sub_3)

less_10 = list(map(lambda x:x+50 ,filter(lambda x:x<10,ls)))
print(less_10)

div = list(filter(lambda x:x%2==0 and x%3==0,ls))
print(div)

sub_5 =list(map(lambda x:x-5,ls))
print(sub_5)
