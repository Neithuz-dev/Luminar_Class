amount = int(input("enter the amount "))
if amount<200:
    charge = 50
elif 200<=amount<=499 :
    charge = 30
else:
    charge = 0
print("The delivery Charge is ",charge)