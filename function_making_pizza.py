#  Importing an entire module

#  This file imports the module contained in the file 
#     function_pizza.py.
#  This file makes two calls to make_pizza()
#  The line 'import function_pizza' tells Python to
#     open the file 'function.pizza' and copy all the
#     functions from it into this program
#  All the functions in 'function_pizza' are now available
#      in this file
#  When we use such import statement to import an entire
#     module, the syntax is: 'module_name.function_name()'
import function_pizza

function_pizza.make_pizza(16, 'pepperoni')
function_pizza.make_pizza(12, 'mushrooms', 'peppers', 'cheese')

#  Importing specific functions

#  General syntax for this approach:
#  ' from module_name import function_0, function_1, function_2
#  With this syntax, we need not use the dot notation when 
#     calling a function. We've explicitly imported the function
#     make_pizza() in the import statement 
from function_pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'peppers', 'cheese')
	
#  Using as to give a Function an Alias

#  If the name of function we're importing conflict with an 
#     existing name in the program or if the function name is 
#     long, we can use an alias
#  Here we give the function make_pizza() an alias mp()
#  Syntax for an alias:
#  from nodule-name import function_name as fn
from function_pizza import make_pizza as mp 

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'pepper', 'cheese')

# Using as to give a Module an Alias

# Providing an alias for a Module
# Syntax for an alias:
# import module_name as mn
import function_pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'cheese, pepper','mushrooms')

#  Importing all functions in a Module

#  Asking Python to import every function in a module by using the
#     asterisk (*)
#  Best not to use this approach when working with larger modules
#     not written by us
#  Python may see several functions or variables with the same name
#     and instead of importing all the functions, overwrite the 
#     functions
#  Syntax: from module_name import *
from function_pizza import *

make_pizza(17, 'pepperoni')
make_pizza(11, 'pepper', 'cheese', 'mushrooms')




