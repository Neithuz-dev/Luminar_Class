class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary =salary

    def increment(self,amount):
        self.salary +=amount
        print(self.name,"New salary:",self.salary)

emp = Employee("Meera",40000)
emp.increment(5000)



