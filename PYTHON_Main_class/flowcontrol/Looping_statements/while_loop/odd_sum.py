#hw print lower to upper odd number sum
lower = int(input("enter the lower: "))
upper = int(input("enter the upper: "))
odd =0
while lower<=upper:
    if lower%2!=0:
        odd+=lower
    lower+=1
print(odd)
