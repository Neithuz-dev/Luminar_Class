num = 145
temp = num
total = 0
while temp>0:
    digit = temp%10
    fact = 1
    for i in range(1,digit+1):
        fact = fact*i
    total += fact
    temp = temp//10
if total == num:
    print("strong number")
else:
    print("not strong number")


