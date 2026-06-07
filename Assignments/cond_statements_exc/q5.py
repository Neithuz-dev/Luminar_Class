# Road Tax Calculator
#
# Write a Python program to find the road tax for a bike based on its price:
#
# If price is above ₹100000, tax = 15% of price
#
# If price is between ₹50000 and ₹100000, tax = 10% of price
#
# If price is ₹50000 or less, tax = 5% of price
bike_price = int(input("enter the bike price: "))
if bike_price > 100000:
    tax = bike_price*0.15
elif bike_price <=100000:
    tax =  bike_price*0.10
elif bike_price<50000 :
    tax = bike_price*0.05
print("the amount of tax",tax)