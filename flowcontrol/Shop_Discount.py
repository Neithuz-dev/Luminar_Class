# Write a Python program to calculate discount based on shopping amount.
#
# Below ₹500 → No discount
#
# ₹500–₹999 → 10% discount
#
# ₹1000–₹4999 → 20% discount
#
# ₹5000 or above → 30% discount

amount = int(input("enter the amount: "))
if amount<500:
    dis=0
elif 500<=amount<=999:
    dis = amount*0.10
elif 1000<=amount<=4999:
    dis = amount*0.20
else:
    dis=amount*0.30
print("The Discount price is ",dis)
