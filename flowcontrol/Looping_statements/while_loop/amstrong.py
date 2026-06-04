n = int(input("enetr the number :"))
temp =n
cube = 0
while temp>0:
    digit =temp%10
    cube = cube+(digit*digit*digit)
    temp = temp//10
if cube == n:
    print("Armstrong")
else:
    print("Not armstrong")