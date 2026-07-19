# 5. Shopping Cart System
# Question
# A customer adds product prices into a shopping cart.
# The program should continue until the user enters 0.
# Find the final cart total.
shopping_cart = 0
product_price = int(input("enter the product price : "))
while product_price>0:
    shopping_cart+=product_price
    product_price = int(input("enter the product price : "))
print("Final cart total : ",shopping_cart)