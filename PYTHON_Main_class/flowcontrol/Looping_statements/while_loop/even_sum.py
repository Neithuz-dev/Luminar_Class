lower = int(input("enter the lower:"))
upper = int(input("enter the upper:"))
even = 0
while lower<=upper:
    if lower%2==0:
        even=even+lower
    lower+=1
print(f"{even}")
#hw print lower to upper odd number sum\
#print lower to upper even and odd number sum