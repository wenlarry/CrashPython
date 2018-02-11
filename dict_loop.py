
# Looping thru all key-value pairs

# Can loop thru all of a dict's key-value pairs, thru its keys
#     or values
user_o = {
	'username': 'elf',
	'first' : 'en',
	'last' : 'fe',
}
#  Write a for loop for a dict, create names for two variables
#  name of dict followed by method items()
#  followed by associated value
#  "\n" ensures that a blank line is inserted before each 
#       key-value pair in the output
for key, value in user_o.items():
    print("\nKey: " + key)
    print("Value: " + value)

fav_lang  ={
	'je': 'python',
	'sa': 'c',
	'ed': 'r',
	'ph': 'ruby',
}
# Code 2
# Use of Use of the variables name and language instead of key
#     and value
for name, lang in fav_lang.items():
    print(name.title() + "'s fav lang is " +
        lang.title() + ".")

# Looping thru all keys in Dict
fav_lang  ={
	'je': 'python',
	'sa': 'c',
	'ed': 'r',
	'ph': 'ruby',
}
#  Make a list of pals

#  Tells Python to pull all the keys from the dict 'fav-lang' and
#      store them in the variable 'name'
#  If pals print greetings
#  To access 'fav_lang', use the name of dict and the current value
#      of name as the key
pals = ['ph', 'sa']
for name in fav_lang.keys():
    print(name.title())

    if name in pals:
        print("Hi" + name.title() +
            ", So yr fav lang is  " +
            fav_lang[name].title() + "!")

# Code 2
# use the keys() method to find out if a particular person was polled
fav_lang  ={
	'je': 'python',
	'sa': 'c',
	'ed': 'r',
	'ph': 'ruby',
}
if 'er' not in fav_lang.keys():
    print("Er, pls poll!")

#  Looping thru a Dict's keys in order

#  This for statement  is where we've wrapped the sorted() function
#      around the dict.keys() method. It tells Python to list all keys
#      in the dict and sort that list before looping
fav_lang  ={
	'je': 'python',
	'sa': 'c',
	'ed': 'r',
	'ph': 'ruby',
}
for name in sorted(fav_lang.keys()):
    print(name.title() +  ", tks for polling")

#  Looping thru all values in Dict

#  Use the values() method to return a list of values without any keys
fav_lang  ={
	'je': 'python',
	'sa': 'c',
	'ed': 'r',
	'ph': 'ruby',
}
print("the following lang mentioned:")
for lang in fav_lang.values():
    print(lang.title())

#  Code 2
#  Use 'SET'
#  For large number of values so that we can see each lang chosen is without
#      repetition 
fav_lang  ={
	'je': 'python',
	'sa': 'c',
	'ed': 'r',
	'ph': 'ruby',
}
print("the following lang mentioned:")
for lang in set(fav_lang.values()):
    print(lang.title())

    
