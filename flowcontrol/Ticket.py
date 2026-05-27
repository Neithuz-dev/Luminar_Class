age = int(input("enter the age fo tha person : "))
actual_price=100
if age<5:
    price =0
elif 5<age and age<=12:
    price = (50*100)/actual_price
elif 13<=age<=59:
    price = actual_price
else:
    price = (30*100)/actual_price

print("The price is",price)


