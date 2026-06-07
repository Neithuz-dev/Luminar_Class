# Ticket Discount Program
#
# Write a Python program to find the ticket price based on a person’s age.
#
# The actual ticket price is ₹100.
#
# If the age is below 5, the ticket is free.
#
# If the age is 5 to 12, they get 50% discount.
#
# If the age is 13 to 59, they pay full price.
#
# If the age is 60 or above, they get 30% discount.
#
# Print the total price to be paid.
actual_price = 100
age = int(input("Enter the age of the person:"))
if age < 5 :
    discount = "free"
elif 5<age<12 :
    discount = (actual_price*50)/100
elif 13<age<59:
    discount = actual_price
else:
    discount = actual_price*0.3
print(f"total price:{discount}")
