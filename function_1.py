#  Functions - named block of codes to do one specific job
#  Makes programs easier to write, read, test and fix

#  def - keyword to inform Python that we're defining a function
#  parentheses hold that info
#  """ - docstring; describes what the function does
#  function call - tells Python to execute the code in the function;
#  Write the name of the function, followed by any info in parantheses
#  The var username in the definition greet_user() is a parameter that
#    the function needs to do its job
# The value 'dude' is an argument; An arg is info that is passed from a
#    function call to a function



def greet_user(username):
    """A simple greeting"""
    print("Hi, " + username.title() + "!")

greet_user('dude') 

# Passing Arguments/Positional Arguments

#  A function definition can have multiple parameters and a function call 
#   may need multiple arguments. 

#  Positional  Arguments - Pythomn must match each arg in the function
#    call  with a parameter in the funtion definition.
#  Postional Arguments - Order Matters. function call to 'hampster'
#    matching animal_type, etc

#  In the function call, the arg ' hamster' is stored in the parameter
#     animal_type and the arg 'haha' is stored in the the parameter
#     pet-name.
def describe_pet(animal_type, pet_name):
	"""Info about a pet"""
	print("\nWe have a  " + animal_type + ".")
	print("Our " + animal_type + "'s name is  " + pet_name.title() + ".")

describe_pet('hampster', 'haha')
describe_pet('dog', 'zeus')

# Keyword Arguments - name-value pair that is paased to a function
def describe_pet(animal_type, pet_name):
	"""Info about a pet"""
	print("\nWe have a  " + animal_type + ".") 
	print("Our " + animal_type + "'s name is  " + pet_name.title() + ".")

describe_pet(animal_type = 'hamster', pet_name = 'haha') 

#  Default values

#  Change the definition of describe_pet() to include a default value 'dog'
#    for animal_type. Now when the function is called with no animal_type
#    specified, Python use the value ;dog for this parameter
#  When an explict arg for animal_type is given, Python ignores the parameter's
#     deault value
def describe_pet(pet_name, animal_type = 'dog'):
    """Info about a pet"""
    print("\nWe have a  " + animal_type + ".")
    print("Our " + animal_type + "'s name is  " + pet_name.title() + ".")

describe_pet(pet_name = 'zeus')
describe_pet('zeus')

describe_pet(pet_name = 'glob', animal_type = 'turkey')

# Equivalent Function Calls

# Positional args, keyword args and default values can all be used together
def describe_pet(pet_name, animal_type = 'dog'):
    """ Info about a pet"""
# a dog named Zeus
describe_pet('zeus') 
describe_pet(pet_name = 'zeus')

#  Avoid Argument Errors
#  Unmatched args occur when we provide fewer or more args than a function needs

#  Return Values

#  The function of get_formatted_name() takes as parameters a first and last name;
#    Combines two names, add a space and stores the result in full_name; Value of
#    full_name is converted to title(), and then returned to the calling line
#  When we call a function that returns a value, we need a var, where the value can 
#     be stored 
#  The returned value here is stored in var musician  
def get_formatted_name(first_name, last_name):
	"""Return a full name formatted"""
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('hk', 'gem')
print(musician)



