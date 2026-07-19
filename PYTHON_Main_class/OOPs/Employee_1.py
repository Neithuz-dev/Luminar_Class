class Employee:
    def __init__(self,name,role,salary):
        self.name = name
        self.role = role
        self.salary = salary
    def info(self):
        print("Employee Name: ",self.name)
        print("Employee role:",self.role)
    def pay(self):
        print("employee salary:",self.salary)
ob1 = Employee("Hanna","Faculty","120000")
ob1.info()
ob1.pay()