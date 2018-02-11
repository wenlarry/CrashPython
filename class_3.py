#  Inheritance

#  The _init_ O Method for a child class

#  When we create a child class, the parent class must be part of the current 
#     file and must appear before the child class.
#  The child class is ElectricCar.Name of parent must be included in the 
#     parentheses of the child class
#  The_init_ method takes in info required to make a Car instance
#  The super() function is a special function that help Python connects the 
#     parent and child classes.  Python calls the _init_ method from the parent
#     class that gives the ElectricCar instance all the attributes of the parent
#     class
#  Make an instance of the electricCar class and store in my_testa. This line 
#     calls the _init_ () method defined in ElectricCar that in turn tells Python
#     to call the the _init_ () method defined in the parent class Car.

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

class ElectricCar(Car):
	"""Aspects of car specific to electric cars"""
	def __init__(self, make, model, year):
		"""Initialize attributes of parent class"""
		super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.desc_name()) 

#  Defining Attributes and Methods for the child class

#  Once we have the child class , we can add new attributes and methods
#    necessary to differentiate the child class from the parent class
#  Add an attribute that this is specific to electric cars eg battery. We store the
#     battery size and write a method that prints the battery description.
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

class ElectricCar(Car):
    """Aspects of car specific to electric cars"""
    def __init__(self, make, model, year):
        """Initialize attributes of parent class"""
        super().__init__(make,model,year)
        self.battery_size = 70

    def describe_battery(self):
        """Print stat describing battery size"""
        print("This car has a " + str(self.battery_size) + "kwh")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.desc_name())
my_tesla.describe_battery()


    




