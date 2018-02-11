#  Working with Classes and Instances

#  Define a method 'desc name()' that put the car make, model, etc into one string
#  To work with the attribute's values, we use self.make, etc
#  Make an instance from Car class and store in the var my_new_car

class Car():
    """Represent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes"""
        self.make = make
        self.model = model
        self.year = year
   
    def desc_name(self):
        """Return a desc name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title() 

my_new_car = Car('audi','a3', 2017)

print(my_new_car.desc_name())

#  Setting a default Value for an Attribute

#  Add an attribute 'odometer_reading' that starts with a value 0.
#     Also add a method read-odometer()
class Car():
    """Represent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 

    def desc_name(self):
        """Return a desc name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title() 

    def read_odometer(self):
        """Show the car's mileage"""
        print("This car has " + str(self.odometer_reading) + "km")

my_new_car = Car('audi', 'a3', 2017)
print(my_new_car.desc_name())
my_new_car.read_odometer()

#  Modifying Attribute Values

#  We can change the attribute's value in three ways. 1) change the value
#    directly thru an instance 2) set the value thru a method 3) increase
#    the value thru a method

#  Modifying the Attribute's value directly
class Car():
    """Represent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 

    def desc_name(self):
        """Return a desc name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title() 

    def read_odometer(self):
        """Show the car's mileage"""
        print("This car has " + str(self.odometer_reading) + "km")

my_new_car = Car('audi', 'a3', 2017)
print(my_new_car.desc_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#  Modifying an Attribute's Value thru a Method

#  Pass the new value to a method that handles the update internally
class Car():
    """Represent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 

    def desc_name(self):
        """Return a desc name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title() 

    def read_odometer(self):
        """Show the car's mileage"""
        print("This car has " + str(self.odometer_reading) + "km")

    def update_odometer(self, mileage):
        """Set odometer reading the a given value"""
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a3', 2017)
print(my_new_car.desc_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

#  Incrementing an Attribute's value thru a Method
class Car():
    """Represent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 

    def desc_name(self):
        """Return a desc name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title() 

    def read_odometer(self):
        """Show the car's mileage"""
        print("This car has " + str(self.odometer_reading) + "km")

    def update_odometer(self, mileage):
        """Set odometer reading the a given value"""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

my_used_car = Car('s', 'outback', 2001)
print(my_used_car.desc_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer() 

my_used_car.increment_odometer(100)
my_used_car.read_odometer()



















