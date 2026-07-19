#print lower to upper even and odd number sum
lower = int(input("enter the lower: "))
upper = int(input("enter the upper: "))
even_temp = 0
odd_temp = 0
while lower<=upper:
    if lower%2==0:
        even_temp+=lower
    else:
        odd_temp+=lower
    lower+=1
print(f"Sum of even number:{even_temp}")
print(f"Sum of odd numbers:{odd_temp} ")
