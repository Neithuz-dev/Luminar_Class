# 4. Water Tank Filling System
# Question
# A water tank can hold 1000 liters.
# Water enters 100 liters every minute.
# Display tank level until the tank becomes full.
tank_capacity = 1000
water_filling = 0
while water_filling < tank_capacity:
    water_filling = water_filling+100
    print(water_filling)
