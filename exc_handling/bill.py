from itertools import count


def total_bill():
    total = 0
    count = 1

    while count <=5:
        try :
            price = float(input(f"enter the price of product"))
            total += price
            count+=1