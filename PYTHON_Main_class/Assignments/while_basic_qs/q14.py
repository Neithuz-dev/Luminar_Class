# 14. Rainfall Monitoring System
# Question
# A weather station records rainfall daily.
# Continue recording until total rainfall reaches 100 cm.
#
total_rainfall = 0
while  total_rainfall < 100:
    rain = int(input("Enter the rainfall: "))
    total_rainfall+=rain
    if total_rainfall>100:
        print("Error,Try again")
    elif total_rainfall==100:
        print("Total rainfall reached 100 cm")