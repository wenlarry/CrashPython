#  Passing an arbitrary number of Arguments

#  When you don't know in advance how many args a function need
#    to accept
#  Asterix * in the parameter toppings tell Python to make an empty
#     tuple called toppings and pack whatever values it receives into
#     this tuple
def make_pizza(*toppings):
    """Summarize the pizza to be made"""
    print("\nMaking a pizza with these toppings:")
    for topping in toppings:
         print(" _ " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'cheese')

#  Using arbitrary keyword Arguments

#  We want an arbitrary number of args, but don't know in advance 
#     what info will be  passed to the function. We can then write
#     functions that accept as many key=value pairs as the calling 
#     statement provides
#  The function build_profile() takes in a first and last name but it
#      accepts an arbitrary number of keyword args
#  The double ** before the parameter **user_info allows Python to 
#      create an empty dict called user-info and pack whatever name-value
#      pairs it receives into the dict.
#  In build_profile(), we make an empty dict called profile to hold the
#      user's profile
#  We loop thru the additional key-value pairs in the dict user-info
#  Return the profile dict to the function call line
#  The function works no matter how many key-value pairs are provided 
#     in the function call
#  We can mix positional, keyword, and arbitrary values in many different
#     ways when writing functions
def build_profile(first, last, **user_info):
	"""Build a dict containing everything we know about a user"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('al', 'einstein',
	                          location = 'princeton',
	                          field = 'physics')
print(user_profile)

#  Styling Functions

#  Functions should have descriptive names and be in lowercase letters
#     and underscores. Modules should be similar
#  Every function should have a concise comment on the function's task
#     The comment should appear immediately after the function definition
#     and use the docstring format
#  Default value for a parameter - no spaces on either side of the equal
#     sign

#  def function_name(para_0, para_1='default value')

#  Same for keyword args in function calls

#  function_name(value_0, para_1='default value')

#  Limit lines of code to 79 characters. If a set of para causes a function's
#    definition to be more than 79 lines, press ENTER after the opening
#    parenthesis on the definition line. On the nest line press TAB twice
#    to separate the list of args from the body of the function, that will be
#    indented one level

#  def function-name(
#          para_0, para_1, para_2,
#          para_3, para_4, para_5):
#      function body ...

#  Program or module with more than one function, separate each by two blank
#     lines
#  All import statements be written at the beginning of a file. Only exception 
#     is if we use comments at the beginning of the file describing the program




	