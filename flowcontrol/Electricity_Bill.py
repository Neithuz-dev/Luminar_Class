# Write a Python program to calculate the electricity bill based on units used:
#
# First 100 units → free
#
# Next 100 units (101–200) → ₹5 per unit
#
# Above 200 units → ₹10 per unit
units = int(input("enter the units:"))
if units<=100:
    amount = 0
    print(amount)
elif units <=200:
    amount = units*5
    print(amount)
elif units >200:
    amount = 200*5+(units*10)
    print(amount)