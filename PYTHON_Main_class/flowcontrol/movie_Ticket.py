age = int(input("enter the age :"))
Ticket_price = 150
if age<5:
    price=0
elif 5<=age<=12:
    price = Ticket_price/2
elif 13<=age<=59:
    price = Ticket_price
else :
    price = Ticket_price*(40/100)
print("The ticket price is ",price)