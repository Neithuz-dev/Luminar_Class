# ATM Withdrawal Simulation
#
# Condition:
#
# Amount must be multiple of 100
#
# Amount ≤ balance
#
# balance = 10000
amount = int(input("enter the amount(only x100): "))
balance = 10000
for i in range(amount<=balance):
    balance-=amount
    print(balance)


