# 10. Electricity Bill Collection
# Question
# An electricity office collects bill payments from customers.
# Continue collecting payments until total collection reaches ₹10000.
total_collection = 0
while total_collection<10000:
    bill = int(input("enetr the amount to pay: "))
    total_collection += bill
    if total_collection>10000:
        print("Error amount exceeds")
    elif total_collection==10000:
        print("total collection reaches ₹10000")
