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

ls= [9,7,4,5,2,1,7,4]
num = list(filter(lambda x:x>3 and x<5,ls))
print(num)

sub_2 = list(map(lambda x:x-2,filter(lambda x:x>4,ls)))
print(sub_2)

