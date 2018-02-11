#  Storing Functions in Modules

#  We can store store functions in a module and them import the module
#     into the main program
#  An import statement tells Python to make the code in module available
#  Storing functions in separate files hides the detailed codes
#  Import functions allow use of the function libraries of other programmers

#  Importing an entire module

#  This module is in a separate file 'function_pizza.py' 
#  This module is to be applied in the file ' function_making_pizza.py'
def make_pizza(size, *toppings):
	"""Summarize the pizza to be made"""
	print("|nMaking a  " + str(size) + 
		"_inch pizza with theses toppings:")
	for topping in toppings:
		print("_ " + topping)
