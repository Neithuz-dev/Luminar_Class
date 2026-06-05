# 8. Fuel Filling Station
# Question
# A bike fuel tank capacity is 15 liters.
# The petrol pump fills fuel continuously.
# Stop when the tank becomes full.
bike_tank = 15
fillings = 0
while fillings < bike_tank:
    fuel_fills = int(input("enter the liter "))
    fillings += fuel_fills
    if fillings == bike_tank:
        print("Stop tank full")
        break
    elif fillings >bike_tank:
        print("Error")
#0<15 true -->2--> 0+2=2 -->2<15  ->3
#2+3 =5 5==15 false