num = int(input("enter the number"))
temp = num
total = 0
while temp > 0:
    digit = temp%10
    fact=1
    for i in range(1,digit+1):
        fact =fact*i
    temp = temp//10
    total +=fact

if num ==total:
    print('strong')