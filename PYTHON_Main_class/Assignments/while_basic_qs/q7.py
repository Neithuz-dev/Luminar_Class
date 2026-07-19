# 7. Daily Savings Tracker
# Question
# A student saves money every day.
# The student wants to save ₹2000.
# Ask saving amount daily until target is reached.
total_amount = 0
while total_amount < 2000: #0<=2000
    saving_amount = int(input("enter the amount :"))
    total_amount+=saving_amount #500 1000 1500 2000
print("Target amount reached")
print("total amount:",total_amount)
