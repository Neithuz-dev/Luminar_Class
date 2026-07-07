class Employee: #Parent Class
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"employee name:{self.name}, salary:{self.salary}")

class Manager(Employee): #Child class from Employee class
    pass

m1 = Manager("Neithal",80000)
m1.show_details()