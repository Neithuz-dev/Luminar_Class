num = int(input("enter the number:"))
sum_count = 0
for i in range(1,num):
    if num%i==0:
        sum_count +=i
    else:
        pass

if sum_count>num:
    print(f"{num} is an Abundant number")
else:
    print("Not Abundant number")