#  Refactoring

#  Improving codes by breaking it into a series of functions that have specific
#     tasks. We refactor by moving the bulk of the logic into one or more 
#     functions. Moving all codes into a function 'greet_user()'
#  As we are using a function, we update the comments with a docstring.
#  The function 'greet_user()' is more that greeting the user, it's also
#     retrieving a stored user name if one exists and prompting for a new user
#      name if one doesn't exist
#  Retrieving a stored username is a separate function. If the file username.json
#     doesn't exist, the function returns 'None'
#  If the username doesn't exist, we move the code that prompts for a ew username
#  Compartmentalization is an essential part of clear coding
import json

def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
	        username = json.load(f_obj)  
    except FileNotFoundError:
	    return None 
    else:
        return username

def get_new_username():
	"""prompt for a new username"""
	username = input("What's your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	"""Greet the user by name"""
username = get_stored_username()
if username:
       print("Welcome back " + username + "!")
else:
    username = get_new_username()
    print("We'll remember you always " + username + "!")

greet_user() 
