balance = 5000
print("1)Check balance\n2)Deposit \n3)Withdraw \n4)Exit")
choice = int(input("enter your choice"))
if choice == 1:
    print("your balance is",balance)
elif choice == 2:
    deposit =int(input("enter the amount to deposit"))
    balance += deposit
    print(f"{deposit} amount deposited")
elif choice ==3:
    withdraw = int(input("enter the amount to withdraw"))
    if withdraw < balance:
      balance -= withdraw
      print(f"{withdraw} amount withdraw")
    else:
        print("Insufficient amount")
elif choice== 4:
    print("ATM exiting")
