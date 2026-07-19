lower = int(input("enter the lower number:"))
upper = int(input("enter the upper:"))
while lower<=upper:
    if lower % 5 == 0:
        print(f"{lower} is divisible by 5")
    lower += 1