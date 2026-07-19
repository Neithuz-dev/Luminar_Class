#Find sum of digits of a number
n = int(input("enter the number: "))
count = len(str(n))
sum =0
for i in range(count):
    if n > 0:
        digit = n%10
        sum+=digit
        n=n//10
print(sum)

