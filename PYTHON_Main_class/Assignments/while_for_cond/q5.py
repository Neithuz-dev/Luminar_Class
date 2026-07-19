# 5.ATM Withdrawal Simulation
#
#  Condition:
#
#  Amount must be multiple of 100
#
#  Amount ≤ balance
balance = int(input("Enter the current balance: "))
amount = int(input("Enter withdrawal amount: "))

if amount % 100 == 0:
    if amount <= balance:
        balance  -= amount
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")
else:
    print("Amount must be a multiple of 100")