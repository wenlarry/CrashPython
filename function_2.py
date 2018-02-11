#  Making an Argument Optional

#  Middle name is optional so listed last and its default value is an
#    empty string
#  Python interprets non-empty string as True, so if middle-name evaluates
#    to True if a middle arg is in the function
#  If no middle name is provided, the empty string fails the if test and the
#     else block runs
     
def get_formatted_name(first_name, last_name, middle_name = ' '):
    """Return a full_name formatted"""	
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name	
    else:
    	full_name = first_name + ' ' + lasr_name
    return full_name.title()

musician = get_formatted_name('jolin', 'yl', 'tsai')
print(musician)

musician = get_formatted_name('elva', 'hsiao')
print(musician)

#  Returning a dictionary

#  Value of first_name stored with the key 'first' and value of last-name stored
#     with the key 'last'. The entire dict representing the person.
def build_person(first_name, last_name, age = ''):
	'''Return a dict about a person'''
	person = {'first': first_name, 'last':last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('gloria', 'gem', age = 28)
print(musician)

#  Function with a loop

#  While loop asks the user to enter name, prompting for first and last name seperately
#  User should be able to quit as easily as possible, so each prompt offers a 'quit'
#  Break offers an exit to the loop at either prompt
def get_formatted_name(first_name , last_name):
    """Return a full name, formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease provide name:")
    print("(enter 'q' anytime to quit)")

    f_name  = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHi, " + formatted_name + "!")











        
    


