n = int(input("number:"))
small = 9
while n>0:
    digit = n%10
    if digit<small:
        small = digit
    n = n//10
print(small)