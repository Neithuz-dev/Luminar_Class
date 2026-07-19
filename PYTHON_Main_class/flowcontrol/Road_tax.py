# Write a Python program to find the road tax for a bike based on its price:
#
# If price is above ₹100000, tax = 15% of price
#
# If price is between ₹50000 and ₹100000, tax = 10% of price
#
# If price is ₹50000 or less, tax = 5% of price
bike_price = int(input("enter the price of the bike"))
if bike_price>100000:
    tax = bike_price*0.15
elif 50000<=bike_price<100000:
    tax = bike_price*0.10
else :
    tax = bike_price*0.05
print("The Tax is", tax)