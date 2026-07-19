# Electricity Bill Calculator
#
# Write a Python program to calculate the electricity bill based on units used:
#
# First 100 units → free
#
# Next 100 units (101–200) → ₹5 per unit
#
# Above 200 units → ₹10 per unit
units = int(input("enter the units: "))
if units <=100:
    bill = 0
elif units<=200:
    bill = (units-100)*5
elif units >200:
    bill = 200*5+(units-200)*10
print("the bill is :",bill)