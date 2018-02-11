#  Importing Module into a Module

#  A separate module for ElectricCar and Battery classes
#  The clas ElectricCar needs access to its parent class Car
#    so we import Car directly into the module

""" A set of classes that can represent electric cars"""
from class_5 import Car

class Battery():
    """Model a battery for an electric car"""
    def _init_(self, battery_size=70):
        """Initialize battery attributes"""
        self.battery_size = battery_size

class ElectricCar(Car):
    """Aspects of car specific to electric cars"""
    def _init_(self, make, model, year):
        """Initialize attributes of parent class"""
        super()._init_ (make, model, year)

        self.battery = Battery()


    



	
