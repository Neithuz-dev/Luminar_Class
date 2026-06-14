# 8.Total Bill Calculation (Shopping Cart)
#
# A customer goes shopping in a store.
#
# Rules:
#
# First, enter the number of items purchased.
#
# Then enter the price of each item.
#
# The total bill is the sum of all item prices.
#
# If the total bill amount is more than ₹5000, the customer gets a 10% discount.
#
# Otherwise, no discount is given.
#
# Display:
#
# Total bill amount
#
# Discount amount
#
# Final amount to be paid
items = int(input("Enter number of items: "))
total_bill = 0

for i in range(items):
    price = int(input("Enter item price: "))
    total_bill += price

if total_bill > 5000:
    discount = total_bill * 0.10
else:
    discount = 0

final_amount = total_bill - discount

print("Total Bill:", total_bill)
print("Discount:", discount)
print("Final Amount to Pay:", final_amount)