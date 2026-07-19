ls = [i for i in range(1,1001)]
ls_5 = [i for i in range(1,501) if i%7==0]
print(ls_5)

ls_3 = [i for i  in range(1,301) if "3" in str(i) ]
print(ls_3)

string = 'practice list comprehension problem in python'
ls_s = len([i for i in string if i ==" "])
print(ls_s)

string = 'practice list comprehension problem in python'
vow = "aeiou"
ls_vow = len([i for i in string if i in vow])
print(ls_vow)

string = 'practice list comprehension problem in python'
ls_word = [i for i in string.split() if len(i)<7]
print(ls_word)

dic = {'bike':500,'car':2700,'jeep':3200,'bus':8000,'van':3400,'cycle':150}
ls_w = [i for i in dic if dic[i]>2500]
print(ls_w)