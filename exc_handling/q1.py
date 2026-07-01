def atm():
     balance =10000

     while True:
         try :
             amount = int(input("enter the amount"))

             if amount>balance:
                 print("Insufficent amount")
             else:
                 balance-= amount
                 print("withdraw")
                 print(balance)
                 break
         except ValueError:
             print("Invalid error")

atm()