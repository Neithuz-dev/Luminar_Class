# Water Bill Calculator
#
# Write a Python program to calculate water bill based on usage.
#
# First 50 liters → ₹2 per liter
#
# Next 100 liters → ₹3 per liter
#
# Above 150 liters → ₹5 per liter

liter = int(input("enter the liter : "))
liter_amount =0
if liter <=50:
    liter_amount = (liter*2)
elif liter<=150: #50x2=100 +50x3=150
    liter_amount = 50*2+(liter-50)*3
elif liter > 150:    #50x2+100x3+50+5
    liter_amount = 50*2+100*3+(liter-150)*5
print("the price",liter_amount)