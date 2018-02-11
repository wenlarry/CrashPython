# Importing Multiple Classes from a Module

from class_5 import Car, ElectricCar

my_beetle  = Car('vw', 'beetle', 2017)
print(my_beetle.desc_name())

my_tesla = ElectricCar('tesla', 'roadster', 2017)
print(my_tesla.desc_name())