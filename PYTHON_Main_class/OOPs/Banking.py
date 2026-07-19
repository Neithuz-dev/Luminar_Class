class  Bank:
    bank_name= "SBI"
    def __init__(self,name,accno):
        self.name = name
        self.accno = accno
        self.minbal =5000
        self.total = self.minbal
    def deposit(self,amount):
        self.amount = amount
        self.total+=self.amount
        print("Bank name:",Bank.bank_name)
        print("Deposited amount:",self.amount)
        print("Updated Account balance:",self.total)

    def withdraw(self,amount_with):
        self.amount_with = amount_with
        if self.total > self.amount_with:
            self.total -= self.amount_with
        else:
            print("insufficent amount")
        print(Bank.bank_name)
        print("Withdraw amount:",self.amount_with)
        print("Remaining Balance:",self.total)


b1 = Bank("Neithal",12345)
b1.deposit(9000)
b1.withdraw(1000)
