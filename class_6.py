#  Importing a single class

#  Import stat tells Python to open 'class_5.py' module
#     and import the class Car

from class_5 import Car

new_car = Car('audi', 'a3', 2017)
print(new_car.desc_name())

new_car.odometer_reading =23
new_car.read_odometer()

