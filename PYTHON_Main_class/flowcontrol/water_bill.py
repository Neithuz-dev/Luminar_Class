# Water Bill Calculator
#
# Write a Python program to calculate water bill based on usage.
#
# First 50 liters → ₹2 per liter
#
# Next 100 liters → ₹3 per liter

# Above 150 liters → ₹5 per liter
liters = int(input("enter the liter usage :"))
if liters <=50:
    amount = liters*2
    print(amount)
elif liters <=150:
    amount= 50*2+(liters-50)*3
    print(amount)
elif liters >150:
    amount =50*2+100*3+(liters-150)*5
    print(amount)
else:
    print("Invalid Liters")
