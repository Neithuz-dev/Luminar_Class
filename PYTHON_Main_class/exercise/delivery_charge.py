amount= int(input('enter the amount:'))
if amount <200:
    charge = 50
elif amount <=499:
    charge = 30
elif amount >=500:
    charge = 0
print(f"The delivery charge is {charge}")