# 2. Mobile Recharge System
# Question
# A customer has ₹500 mobile balance.
# The user enters recharge pack amounts continuously.
# Stop when balance becomes 0 or negative.
balance = 500
while balance > 0:
    recharge = int(input("Enter recharge pack amount: "))
    balance -= recharge
    print("Remaining balance:", balance)

print("Balance exhausted.")