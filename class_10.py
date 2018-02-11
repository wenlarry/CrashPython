# #  Importing a Module into a Module

#  When we store your classes in several modules, we may find 
#     that a class in one module depends on a class in another
#     module. We can import the the required class into the first
#     module

#  A separate module containing ElectricCar and Battery classes created
#     in class__9.py
#  This is a separate module for Car class

""" A class that can represent a car"""
class Car():
    """Represent a car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def desc_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self. model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + "km'")

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self. odometer_reading = mileage

        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, km):
        self.odometer_reading += km



	
