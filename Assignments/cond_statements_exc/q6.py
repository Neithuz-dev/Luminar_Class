# Speed Fine Calculator
#
# Write a Python program to calculate the fine based on a car’s speed.
#
# Speed ≤ 60 km/h → No fine
#
# Speed 61 – 80 km/h → ₹100 fine
#
# Speed > 80 km/h → ₹500 fine
speed = int(input("enter the speed: "))
if speed <=60:
    fine = 0
elif speed<=80:
    fine = 100
elif speed >80:
    fine = 500
else:
    print("invalid")
print('Fine is ', fine)