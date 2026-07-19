n = int(input("enetr the number:"))
count = 1
while n>0:
    digit = n%10
    count = count*digit
    n=n//10
print(count)
    