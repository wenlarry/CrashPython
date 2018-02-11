#  Importing Classes

#  Importing a single class & Storing Multiple Classes
#     in a Module

#  A module containing code representing a car
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

class Battery():
    """Model a battery for an electric car"""

    def __init__(self, battery_size=70):
        """Initialize battery attributes"""
        self.battery_size = battery_size

    def range(self):
        """ Print a stat about the range of the battery"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approx " + str(range)
        message += "  km on full charge"
        print(message) 

class ElectricCar(Car):
    """Aspects of car specific to electric cars"""
    def _init_(self, make, model, year):
        """Initialize attributes of parent class"""
        super()._init_ (make, model, year)

        self.battery = Battery()
            	