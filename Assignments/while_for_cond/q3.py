# Find sum of digits of a number
num = int(input("enter the number: "))
count = len(str(num))
sum = 0
for i in range(count):
    digit = num%10
    sum +=digit
    num=num//10
print("sum of digits of a number",sum)