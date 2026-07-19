# Question: Create a Class in Python
#
# Create a class called Car.
#
# Add the following properties:
# brand
# model
# year
#
# Create two methods:
# cardetails() – Print the brand and model of the car.
#
# yeardetails() – Print the manufacturing year of the car.
# Create two objects of the Car class.
#
# Assign values to the properties using the objects.
class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def cardetails(self):
        print("Brand Model:",self.brand)
        print("Model:",self.model)
    def yeardetails(self):
        print("manufacturing year:",self.year)

ob1 = Car("Toyota","suv","2020")
ob2 = Car("TATA","suv","2026")
ob1.cardetails()
