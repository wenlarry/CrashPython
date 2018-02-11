# Importing a Module into a Module

# We import Car from its module and ElectricCar
#    from its module
from class_10 import Car
from class_9 import ElectricCar

my_beetle = Car('vw', 'beetle', 2017)
print(my_beetle.desc_name())

my_testa = ElectricCar('tesla', 'roadster', 2017)



