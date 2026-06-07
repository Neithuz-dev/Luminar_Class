# Shopping Bill with Membership Discount
#
# A store gives discounts based on the total amount and membership type.
#
#
# amount > ₹2000 and membership = "Gold"	        discount - 20%
# amount > ₹1000 and membership = "Silver"	discount - 10%
# Otherwise	                                discount -  5%
amount = int(input("enter the amount: "))
membership = input("enter the type: ")
if amount > 2000 and membership == "gold":
    dis = amount*0.20
elif amount >1000 and membership == "silver":
    dis = amount*0.10
else:
    dis = amount*0.05
print("The discount amount is",dis)