# Delivery Charge Calculator
#
# Write a Python program to calculate the delivery charge based on the shopping amount.
#
# If the amount is below ₹200, delivery charge is ₹50.
#
# If the amount is ₹200 to ₹499, delivery charge is ₹30.
#
# If the amount is ₹500 or more, delivery is free.
#
# Print the delivery charge.
amount = int(input("enter the Shopping amount: "))
if amount<200:
    charge = 50
elif 200<=amount<499:
    charge = 30
else:
    charge = 0
print(f"The total amount with delivery charge: {amount+charge}")