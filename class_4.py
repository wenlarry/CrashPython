#  Overriding Methods from the Parent Class

#  Define a method in the child class with the same
#     name as the method we want o override in the
#     parent class
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

    def ElectricCar(Car):  
        """Aspects of car specific to electric cars"""
        def __init__(self, make, model, year):
            """Initialize attributes of parent class"""
        super()._init_ (make, model, year)

        def fill_gas_tank():
            """Electric cars have no gas tanks"""
            print("This car doesn't need a gas tank")

#  Instances as Attributes

#  We can move attributes and  methods to a special class
#     Battery and then use a Battery instance as an attribute
#     in the ElectricCar class
#  Define a new class 'Battery' that doesn't inherit from any other
#     class and has one para battery_size.The method desc_battery
#     has been moved to this class

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

    def desc_battery(self):
        """Print a stat on battery size"""
        print("This car has a  " + str( self.battery_size) + "kwh battery")

class ElectricCar(Car):
    """Aspects of car specific to electric cars"""
    def __init__(self, make, model, year):
        """Initialize attributes of parent class"""
        super().__init__(make, model, year)

        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2017) 

print(my_tesla.desc_name())
my_tesla.battery.desc_battery()
my_tesla.battery.range() 

#  Model Real_World Objects

#  Is the range of an electric car a property of the battery or of the car
#  If describing one car; associate method range() with the Battery class
#  If describing an entire line of cars; move range() to ElectricCar class
#  Alternatively, we could maintain the association of the range() method
#     with the battery class but pass it a para eg car_model.
#  Thinking about representing the World in Codes !


